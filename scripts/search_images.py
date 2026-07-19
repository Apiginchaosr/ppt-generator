#!/usr/bin/env python3
"""
Image Search Helper — Dual-channel image sourcing for PPT generation.

Strategy:
- Channel 1: Web search for real photos (via available search tools)
- Channel 2: AI generation for styled/abstract images

Usage:
    python search_images.py --query "business meeting" --style "realistic" --count 3 --output-dir ./images/
"""

import argparse
import json
import os
import sys
import hashlib
import time
from pathlib import Path

try:
    import requests
    HAS_REQUESTS = True
except ImportError:
    HAS_REQUESTS = False


# ---------------------------------------------------------------------------
# Image source recommendations
# ---------------------------------------------------------------------------
IMAGE_SOURCES = {
    "realistic": {
        "primary": "web_search",
        "keywords_zh": ["实拍", "高清", "真实照片"],
        "keywords_en": ["real photo", "high resolution", "professional"],
        "recommended_sites": ["unsplash.com", "pexels.com", "pixabay.com"],
    },
    "business": {
        "primary": "web_search",
        "keywords_zh": ["商务", "专业", "企业"],
        "keywords_en": ["business", "professional", "corporate"],
        "recommended_sites": ["unsplash.com", "pexels.com", "linkedin.com"],
    },
    "anime": {
        "primary": "ai_generation",
        "keywords_zh": ["二次元", "动漫风格", "插画"],
        "keywords_en": ["anime style", "illustration", "cartoon"],
        "recommended_sites": [],
    },
    "minimalist": {
        "primary": "ai_generation",
        "keywords_zh": ["极简", "抽象", "几何"],
        "keywords_en": ["minimalist", "abstract", "geometric"],
        "recommended_sites": [],
    },
    "general": {
        "primary": "web_search",
        "keywords_zh": [],
        "keywords_en": [],
        "recommended_sites": ["unsplash.com", "pexels.com", "pixabay.com"],
    },
}


# ---------------------------------------------------------------------------
# Video source recommendations
# ---------------------------------------------------------------------------
VIDEO_SOURCES = {
    "free": [
        {"name": "Pexels Video", "url": "https://www.pexels.com/videos/", "best_for": "通用背景、自然风光、商业场景"},
        {"name": "Pixabay Video", "url": "https://pixabay.com/videos/", "best_for": "通用素材、动画背景"},
        {"name": "Coverr", "url": "https://coverr.co/", "best_for": "网站/PPT背景循环视频"},
        {"name": "Mixkit", "url": "https://mixkit.co/free-stock-video/", "best_for": "高质量免费素材"},
    ],
    "professional": [
        {"name": "Storyblocks", "url": "https://www.storyblocks.com/video", "best_for": "商业级素材，需订阅"},
        {"name": "Artgrid", "url": "https://artgrid.io/", "best_for": "电影级素材，需订阅"},
        {"name": "Envato Elements", "url": "https://elements.envato.com/video", "best_for": "丰富素材库，订阅制"},
    ],
}


# ---------------------------------------------------------------------------
# Search query builder
# ---------------------------------------------------------------------------
def build_search_query(topic: str, style: str, lang: str = "auto") -> str:
    """Build an optimized search query for the given topic and style."""
    source_info = IMAGE_SOURCES.get(style, IMAGE_SOURCES["general"])
    primary = source_info["primary"]

    if lang == "zh" or any('一' <= c <= '鿿' for c in topic):
        keywords = source_info["keywords_zh"]
    else:
        keywords = source_info["keywords_en"]

    # Combine topic with style keywords
    parts = [topic] + keywords[:2]
    return " ".join(parts)


def get_style_recommendation(style: str, lang: str = "zh") -> dict:
    """Get the sourcing strategy recommendation for a style."""
    info = IMAGE_SOURCES.get(style, IMAGE_SOURCES["general"])
    return {
        "style": style,
        "primary_channel": info["primary"],
        "recommended_sites": info["recommended_sites"],
        "search_query_template": build_search_query("{}", style, lang),
    }


# ---------------------------------------------------------------------------
# Generate search guidance for the SKILL
# ---------------------------------------------------------------------------
def generate_search_guidance(config: dict) -> str:
    """Given a PPT config, output guidance for image sourcing."""
    lines = ["## Image Sourcing Plan\n"]
    style = config.get("meta", {}).get("image_style", "general")
    lang = config.get("meta", {}).get("language", "zh")
    rec = get_style_recommendation(style, lang)

    lines.append(f"**Style**: {style}")
    lines.append(f"**Primary channel**: {rec['primary_channel']}")
    if rec["recommended_sites"]:
        lines.append(f"**Recommended sites**: {', '.join(rec['recommended_sites'])}")
    lines.append("")

    # Per-slide image needs
    for i, slide in enumerate(config.get("slides", [])):
        image = slide.get("image")
        if image:
            alt = image.get("alt", "")
            desc = image.get("description", alt)
            query = build_search_query(desc or alt, style, lang)
            lines.append(f"### Slide {i+1}: {slide.get('title', 'Untitled')}")
            lines.append(f"- Search query: `{query}`")
            lines.append(f"- Channel: {rec['primary_channel']}")
            if rec["recommended_sites"]:
                lines.append(f"- Sites: {', '.join(rec['recommended_sites'])}")
            lines.append("")

    return "\n".join(lines)


def generate_video_recommendations(scenario: str, lang: str = "zh") -> str:
    """Generate video sourcing recommendations based on scenario."""
    lines = []
    if lang == "zh":
        lines.append("## 视频素材推荐\n")
        lines.append(f"根据您的「{scenario}」场景，建议以下视频素材来源：\n")
    else:
        lines.append("## Video Source Recommendations\n")
        lines.append(f"Based on your '{scenario}' scenario:\n")

    lines.append("### 免费素材 (Free)")
    for src in VIDEO_SOURCES["free"]:
        lines.append(f"- **{src['name']}**: {src['best_for']} → {src['url']}")

    if scenario in ("business", "creative"):
        lines.append("\n### 专业素材 (Professional)")
        for src in VIDEO_SOURCES["professional"]:
            lines.append(f"- **{src['name']}**: {src['best_for']} → {src['url']}")

    lines.append("\n您也可以直接提供本地视频文件路径，我会将其嵌入PPT中。")
    return "\n".join(lines)


# ---------------------------------------------------------------------------
# Main
# ---------------------------------------------------------------------------
def main():
    parser = argparse.ArgumentParser(description="Image search helper for PPT generation")
    parser.add_argument("--query", help="Search query for images")
    parser.add_argument("--style", default="general",
                        choices=["realistic", "business", "anime", "minimalist", "general"],
                        help="Visual style preference")
    parser.add_argument("--count", type=int, default=3, help="Number of images to find")
    parser.add_argument("--output-dir", default="./ppt_images", help="Directory to save images")
    parser.add_argument("--lang", choices=["zh", "en", "auto"], default="auto")
    parser.add_argument("--config", help="JSON config file (generates sourcing plan)")
    parser.add_argument("--video-recs", action="store_true", help="Print video recommendations")
    parser.add_argument("--scenario", default="general", help="PPT scenario for video recs")
    args = parser.parse_args()

    if args.config:
        with open(args.config, "r", encoding="utf-8") as f:
            config = json.load(f)
        print(generate_search_guidance(config))
        if args.video_recs:
            print(generate_video_recommendations(
                config.get("meta", {}).get("scenario", "general"),
                config.get("meta", {}).get("language", "zh")
            ))
        return

    if args.query:
        query = build_search_query(args.query, args.style, args.lang)
        rec = get_style_recommendation(args.style, args.lang)

        print(f"Style: {args.style}")
        print(f"Channel: {rec['primary_channel']}")
        print(f"Search query: {query}")
        if rec["recommended_sites"]:
            print(f"Sites: {', '.join(rec['recommended_sites'])}")
        print()
        print("Use your available web search tool to find images with the above query.")
        print("Then download matching images to the output directory.")
        print(f"Output dir: {os.path.abspath(args.output_dir)}")
        return

    # No action specified
    parser.print_help()


if __name__ == "__main__":
    main()

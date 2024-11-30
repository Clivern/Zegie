# Copyright 2025 Clivern
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#     https://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.

import os
from zegie.images import Unsplash


def main():
    # Initialize Unsplash with your API access key
    # Get your access key from https://unsplash.com/developers
    access_key = os.getenv("UNSPLASH_ACCESS_KEY")

    if not access_key:
        print("Error: UNSPLASH_ACCESS_KEY environment variable is not set.")
        print("Please set it with your Unsplash API access key.")
        print("Get one at https://unsplash.com/developers")
        return

    unsplash = Unsplash(access_key=access_key)

    # Example 1: Basic search
    print("Example 1: Basic Search")
    print("=" * 60)
    try:
        images = unsplash.search("nature", per_page=3)
        print(f"Found {len(images)} image(s):\n")

        for i, image in enumerate(images, 1):
            print(f"Image {i}:")
            print(f"  Description: {image.get('description') or image.get('alt_description') or 'N/A'}")
            print(f"  Dimensions: {image.get('width')}x{image.get('height')} pixels")
            if image.get("user"):
                print(f"  Photographer: {image['user'].get('name', 'N/A')}")
            print(f"  URL: {image.get('urls', {}).get('regular', 'N/A')}")
            print()
    except Exception as e:
        print(f"Error: {e}\n")

    # Example 2: Search with filters
    print("Example 2: Search with Filters")
    print("=" * 60)
    try:
        images = unsplash.search(
            "sunset", per_page=3, orientation="landscape", order_by="popular"
        )
        print(f"Found {len(images)} landscape sunset image(s):\n")

        for i, image in enumerate(images, 1):
            desc = image.get("description") or image.get("alt_description") or "N/A"
            if len(desc) > 60:
                desc = desc[:60] + "..."
            print(f"{i}. {desc}")
            print(f"   {image.get('urls', {}).get('regular', 'N/A')}")
    except Exception as e:
        print(f"Error: {e}\n")


if __name__ == "__main__":
    main()

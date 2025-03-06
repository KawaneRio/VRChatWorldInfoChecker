import requests
import re

def extract_world_id(url):
    """Extracts the VRChat world ID"""
    match = re.search(r"wrld_[a-zA-Z0-9-]{36}", url)  # Regular Expressions "wrld_" followed by 36 alphanumeric characters and a dash
    if match:
        return match.group(0)  # Returns the matched world ID
    else:
        return None  # No valid world ID found

def get_vrchat_world_details(world_url):
    # Extract world ID
    world_id = extract_world_id(world_url)
    if not world_id:
        return "💀💀💀Bro I see no wrld_xxxxxxxx-xxxx-xxxx-xxxx-xxxxxxxxxxxx here💀💀💀"

    url = f"https://api.vrchat.cloud/api/1/worlds/{world_id}"

    # 🍪🍪🍪🍪🍪DON'T FORGET TO GIVE ME YOUR AUTHCOOKIES HERE!!!!!🍪🍪🍪🍪🍪
    cookies = {
        "auth": "authcookie_xxxxxxxx-xxxx-xxxx-xxxx-xxxxxxxxxxxx"
    }

    # VRChat requires a User-Agent header
    headers = {
        "User-Agent": "IjustWannaKnowHowtheVRChatAPIworks_AlsoPleaseHireMeVRChat_PythonScript_by_KawaneRio/1.0 (contact: rio.kawane@gmail.com)"
    }

    response = requests.get(url, cookies=cookies, headers=headers)

    if response.status_code == 200:
        world_data = response.json()
        
        # Extract details
        world_name = world_data.get("name", "World Name Unknown")
        author_name = world_data.get("authorName", "Author Unknown")
        capacity = world_data.get("capacity", "Capacity Unknown")
        created_at = world_data.get("created_at", "Created at Unknown Time")
        updated_at = world_data.get("updated_at", "Updated at Unknown Time")
        description = world_data.get("description", "Description does not Exist")

        # Check Platform Compatibility
        platforms = set()
        for package in world_data.get("unityPackages", []):
            platform = package.get("platform", "unknown")
            platforms.add(platform)

        if "android" in platforms and "standalonewindows" in platforms:
            compatibility = "cross_platform"
        elif "android" in platforms:
            compatibility = "android_only"
        elif "standalonewindows" in platforms:
            compatibility = "standalonewindows_only"
        else:
            compatibility = "I see nothin' here; did you forget to modify the script and give me your authcookie?🍪"

        # Print the details
        world_info = f"""
-----ｷﾘﾄﾘﾊｼﾞﾒ----✂ ----------
🌍 world_name 🌍
{world_name}

✍️ author_name ✍️
{author_name}

👥 capacity 👥
{capacity}

📅 created_at 📅
{created_at}

💾 updated_at 💾
{updated_at}

📝 description 📝
{description}

📱 compatibility 📱
{compatibility}

-----ｷﾘﾄﾘｵﾜﾘ----✂ ----------
"""
        return world_info

    else:
        return f"💀💀💀Error: {response.status_code}, {response.text}"

# ---- Keep the script running until the user exits ----
while True:
    world_url = input("\nEnter VRChat World URL or World ID (or type 'exit' to quit): ").strip()

    if world_url.lower() in ["exit", "quit"]:
        break  # EXIT THE LOOP

    print(get_vrchat_world_details(world_url))

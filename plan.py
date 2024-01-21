"""
MASTER PLAN

get all the name:link in a variable => data
data.setdefault(movie, {})
    1st function: use the link to find no.of seasons
    data[movie].setdefault(sn, {})
        2nd function: find all the episode:link
        data[movie][sn].setdefault("episode": "thelink")



name = data
add movie first,
add the seasons
add the episode + links
repeat the loop

data.setdefault(movie, {})
data[movie].setdefault(sn, {})
data[movie][sn].setdefault("episode": "thelink")
"""

movie = {"movie1": {"sn2": {"episode1": "link1", "episode2": "link2", "episode3": "link3"},
                    "sn1": {"episode1": "link1", "episode2": "link2", "episode3": "link3"}},

         "movie2": {"sn2": {"episode1": "link1", "episode2": "link2", "episode3": "link3"},
                    "sn1": {"episode1": "link1", "episode2": "link2", "episode3": "link3"}},

         "movie3": {"sn2": {"episode1": "link1", "episode2": "link2", "episode3": "link3"},
                    "sn1": {"episode1": "link1", "episode2": "link2", "episode3": "link3"}}
         }

link_dict = {'Yoh Christmas': 'https://o2tvseries2.com/Yoh-Christmas/', 'Yu Yu Hakusho': 'https://o2tvseries2.com/Yu-Yu-Hakusho/', '1670': 'https://o2tvseries2.com/1670/', '30 Coins': 'https://o2tvseries2.com/30-Coins/', 'Yosi - The Regretful Spy': 'https://o2tvseries2.com/Yosi-The-Regretful-Spy/', '4Ever': 'https://o2tvseries2.com/4Ever/', 'Young Love': 'https://o2tvseries2.com/Download-Young-Love-otvsqhft/', 'Zatima': 'https://o2tvseries2.com/Zatima/', '6ixtynin9 - The Series': 'https://o2tvseries2.com/Download-6ixtynin9-The-Series-otv2r5gx/', '61st Street': 'https://o2tvseries2.com/61st-Street/', '1985': 'https://o2tvseries2.com/1985/', 'Year Of': 'https://o2tvseries2.com/Year-Of/', 'Yellowjackets': 'https://o2tvseries2.com/Yellowjackets/', 'Yakitori - Soldiers of Misfortune': 'https://o2tvseries2.com/Yakitori-Soldiers-of-Misfortune/', 'Young Sheldon': 'https://o2tvseries2.com/Young-Sheldon-9-otvbwlaf/', '911 Lone Star': 'https://o2tvseries2.com/911-Lone-Star/', '911': 'https://o2tvseries2.com/911/', 'Yonder': 'https://o2tvseries2.com/Yonder/', 'Your Honor': 'https://o2tvseries2.com/Your-Honor/', 'You': 'https://o2tvseries2.com/You-9-otv2g1z8/', 'YOLO - Crystal Fantasy': 'https://o2tvseries2.com/YOLO-Crystal-Fantasy/', '1923': 'https://o2tvseries2.com/1923/', 'Young Rock': 'https://o2tvseries2.com/Download-Young-Rock/', 'You and Me': 'https://o2tvseries2.com/You-and-Me-r9/', 'Yellowstone': 'https://o2tvseries2.com/Yellowstone/', '1899': 'https://o2tvseries2.com/1899/', 'Zootopia': 'https://o2tvseries2.com/Zootopia/', 'Young Royals': 'https://o2tvseries2.com/Young-Royals/', '11 Minutes': 'https://o2tvseries2.com/11-Minutes/', 'You are Nothing Special': 'https://o2tvseries2.com/You-are-Nothing-Special/', 'Young Justice': 'https://o2tvseries2.com/Young-Justice-otvsqv6p/', '42 Days of Darkness': 'https://o2tvseries2.com/42-Days-of-Darkness/', 'Yakamoz S-245': 'https://o2tvseries2.com/Yakamoz-S-245/', '1883': 'https://o2tvseries2.com/1883/', 'Young Wallander': 'https://o2tvseries2.com/Young-Wallander/', '4400': 'https://o2tvseries2.com/4400/', 'You Dont Know Me': 'https://o2tvseries2.com/You-Dont-Know-Me/', '8 Witnesses': 'https://o2tvseries2.com/8-Witnesses/', 'Y - The Last Man': 'https://o2tvseries2.com/Y-The-Last-Man/', 'Younger': 'https://o2tvseries2.com/Younger-9/', 'Zoeys Extraordinary Playlist': 'https://o2tvseries2.com/Zoeys-Extraordinary-Playlist-2/', 'Yasuke': 'https://o2tvseries2.com/Yasuke/', 'Zero': 'https://o2tvseries2.com/Zero/', 'Zero Chill': 'https://o2tvseries2.com/Zero-Chill/', '50M2': 'https://o2tvseries2.com/50M2/', '3 caminos': 'https://o2tvseries2.com/3-caminos/', 'Yankee Hustle': 'https://o2tvseries2.com/Yankee-Hustle/', '3 Percent': 'https://o2tvseries2.com/3-Percent/', 'You Me Her': 'https://o2tvseries2.com/You-Me-Her-9/', '13 Reasons Why': 'https://o2tvseries2.com/13-Reasons-Why-8/', 'ZeroZeroZero': 'https://o2tvseries2.com/ZeroZeroZero-1/', 'You Cannot Hide': 'https://o2tvseries2.com/You-Cannot-Hide/', '3Below - Tales of Arcadia': 'https://o2tvseries2.com/3Below-Tales-of-Arcadia/', 'Years and Years': 'https://o2tvseries2.com/Years-and-Years/', 'Youre the Worst': 'https://o2tvseries2.com/Youre-the-Worst-9/', 'Z Nation': 'https://o2tvseries2.com/Z-Nation-8/', '5th Ward': 'https://o2tvseries2.com/5th-Ward/', '12 Monkeys': 'https://o2tvseries2.com/12-Monkeys-8/', 'You Are Wanted': 'https://o2tvseries2.com/You-Are-Wanted-9/', '9JKL': 'https://o2tvseries2.com/9JKL-8/', 'Zoo': 'https://o2tvseries2.com/Zoo-8/', '24 Legacy': 'https://o2tvseries2.com/24-Legacy-8/', '2 Broke Girls': 'https://o2tvseries2.com/2-Broke-Girls-9/', '24': 'https://o2tvseries2.com/24-8-otvof2mk/'}
print(len(link_dict))


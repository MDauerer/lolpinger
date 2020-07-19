from pythonping import ping
import os

os.system("cls")

COLORS = {
"black":"\u001b[30;1m",
"red": "\u001b[31;1m",
"green":"\u001b[32m",
"yellow":"\u001b[33;1m",
"blue":"\u001b[34;1m",
"magenta":"\u001b[35m",
"cyan": "\u001b[36m",
"white":"\u001b[37m",
"yellow-background":"\u001b[43m",
"black-background":"\u001b[40m",
"cyan-background":"\u001b[46;1m",
}

def colorText(text):
    for color in COLORS:
        text = text.replace("[[" + color + "]]", COLORS[color])
    return text

response_list = ping('104.160.141.3', size = 40, count = 20)

#average ping
avg_ping = str(response_list.rtt_avg_ms)
avg_ping_color = "white"

if float(avg_ping) < 50:
    avg_ping_color = "green"

elif float(avg_ping) > 50 and float(avg_ping) < 100:
    avg_ping_color = "yellow"

else:
    avg_ping_color = "red"

avg_ping = "[[" + avg_ping_color + "]]" + avg_ping + "[[white]]"
colored_avg_ping = colorText(avg_ping)


#maxp ping
max_ping = str(response_list.rtt_max_ms)
max_ping_color = "white"

if float(max_ping) < 50:
    max_ping_color = "green"

elif float(max_ping) > 50 and float(max_ping) < 100:
    max_ping_color = "yellow"

else:
    max_ping_color = "red"

max_ping = "[[" + max_ping_color + "]]" + max_ping + "[[white]]"
colored_max_ping = colorText(max_ping)

#lowest ping
min_ping = str(response_list.rtt_min_ms)
min_ping_color = "white"

if float(min_ping) < 50:
    min_ping_color = "green"

elif float(min_ping) > 50 and float(min_ping) < 100:
    min_ping_color = "yellow"

else:
    min_ping_color = "red"

min_ping = "[[" + min_ping_color + "]]" + min_ping + "[[white]]"
colored_min_ping = colorText(min_ping)


print("Your average ping to LOL EUW is: " + colored_avg_ping + " ms")
print("Your highest ping to LOL EUW is: " + colored_max_ping + " ms")
print("Your lowest ping to LOL EUW is: " + colored_min_ping + " ms")
wait = input ('Press Enter to continue')

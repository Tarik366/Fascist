from bs4 import BeautifulSoup
import requests

t = requests.get("https://discord.com/developers/applications/855326262075457546/bot")
to = BeautifulSoup(t.text,"html5lib")
tok = to.find("div",{"class":"flex-2S1XBF"}).find("div")
print(tok)
translater = "Daha önce başka bir ekipte çalıştın mı?\n\nBağımsız da olsa deneyimin var mı?\n\nİngilizce seviyen nedir?\n\nEn çok hangi tür mangaları seviyorsun?\n\nHaftada kaç bölüm çevirebilirsin?"
editor = "Daha önce başka bir ekipte çalıştın mı?\n\nBağımsız da olsa deneyimin var mı?\n\nHaftada kaç bölüm editleyebilirsin?\n\nPhotoshop seviyene 5 üzerinden puan verebilir misin?"

#gifs
like = "https://c.tenor.com/S_D9CVgOAv4AAAAM/konosuba-kazuma.gif"
rage = "https://c.tenor.com/7eWRtQE4DMEAAAAM/konosuba-kazuma.gif"
anakuzusu = "https://c.tenor.com/7y0-KV0znhgAAAAM/aqua-konosuba.gif"
cry = "https://c.tenor.com/o0lrdNm2BawAAAAM/aqua-cry-cute-aqua.gif"
freakout = "https://c.tenor.com/1NybbVnbzesAAAAM/konosuba-konosuba-aqua-freakout.gif"
haa = "https://c.tenor.com/EqXxr-nY99EAAAAM/kono-subarashii-sekai-ni-shukufuku-wo-konosuba.gif"
o7konosuba = "https://c.tenor.com/P7LP_L_qJp0AAAAM/konosuba.gif"
nomnom = "https://c.tenor.com/rgH7ck0GdCoAAAAM/aqua-konosuba.gif"
like2x = "https://c.tenor.com/CHJ0vddYoxkAAAAM/aqua-konosuba.gif"
shock = "https://c.tenor.com/AkDIq-gCF8cAAAAM/anime-shocked.gif"
o7 = "https://c.tenor.com/LdAr7ZnMsaMAAAAM/yes-sir-yes-boss.gif"
vatozsax = "https://c.tenor.com/1IMoSGd3FS4AAAAC/seal-sax.gif"
dwayne = "https://c.tenor.com/160ZP1AognIAAAAM/dwayne-johnson-looking.gif"
hatsoff = "https://c.tenor.com/YSRFoU5qT64AAAAC/joseph-stalin-hats-off.gif"
capitalism = "https://c.tenor.com/Dqk0z0OmEiYAAAAS/must-crash-capitalism-capitalism.gif"
soviet = "https://c.tenor.com/OALv3DkcHVgAAAAC/soviet-union.gif"
sikin = "https://cdn.discordapp.com/attachments/798641429056454689/942869862831775754/download.jpg"
sosyalistsusamuru = "https://c.tenor.com/I1tCwOlXtEYAAAAC/monday-wtf.gif"
fire = "https://c.tenor.com/neKANiuuxFIAAAAM/banana-fish-ash-banana-fish.gif"
marcharmy = "https://c.tenor.com/vuImAFj69HYAAAAS/marching-army.gif"
irumadance = "https://c.tenor.com/vebF_E3Vj8EAAAAM/anime-dance.gif"
taaminandım = "https://c.tenor.com/TUEKF4Ih-dYAAAAM/tamam-inandim.gif"
kaptansummary = "https://cdn.discordapp.com/attachments/798641429056454689/940025498023649290/unknown.png"
stare = "https://c.tenor.com/GG_95p7JLlwAAAAM/kevin-hart-stare.gif"
GreatPurge = "https://cdn.discordapp.com/attachments/798641429056454689/939674311545991208/download.jpg"
napim = "https://c.tenor.com/NEtIKU9ma_8AAAAC/maxmarine-napim.gif"
napimdiyeni = "https://media.discordapp.net/attachments/799906810072662026/837761017207193600/giphy.gif"
hatayapar = "https://cdn.discordapp.com/attachments/947930185670467635/948296093702185010/csdewsd.jpg"
nazifokları = "https://cdn.discordapp.com/attachments/947930185670467635/948296286354935848/images.jpg"
darkside = "https://media.discordapp.net/attachments/798641429056454689/937459004727230524/8602a4ce228b28f4daff90a23fc169f96ea1871186325d043c95f3ade4e0ca69.gif"
troll = "https://c.tenor.com/GryShD35-psAAAAM/troll-face-creepy-smile.gif"
yahudiler = "https://cdn.discordapp.com/attachments/947930185670467635/948298700529233980/cover6.jpg"
balanced = "https://c.tenor.com/Hqyg8s_gh5QAAAAM/perfectly-balanced-thanos.gif"
jii = "https://media.discordapp.net/attachments/798641429056454689/935234453381464084/hanakokun___Tumblr.gif"
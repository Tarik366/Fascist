import os.path
import random
from unicodedata import name
from discord import *
from discord import app_commands
from discord.ext import commands
from Vars import *
from Sözler.Hitler import *
from Sözler.Atatürk import *
from Sözler.Lenin import *
from Sözler.Stalin import *
from Sözler.Cengiz import *
from Sözler.CelalŞengör import *
from Sözler.MeteHan import *
from Sözler.Einstein import *
from propaganda import *
from hoi4tips import *
from bs4 import BeautifulSoup
import requests
import json
from PIL import Image
from PIL import ImageFont
from PIL import ImageDraw 
import numpy as np
from dotenv.main import load_dotenv

load_dotenv()
uid = 798641429056454686

class aclient (Client):
    def __init__(self):
        super().__init__(intents=Intents.default())
        self.synced = False

    async def on_ready(self):
        await self.wait_until_ready()
        if not self.synced:
            await Bot.sync(guild = Object(id = uid)) 
            self.synced = True
        print (f"{self.user}'a bağlanıldı.")


client = aclient()
Bot = app_commands.CommandTree(client)
bot = commands.Bot(command_prefix="!", intents=Intents.default())
tür = "vatoz"

# Help komutu

@Bot.command(name = "yardım", description = "Bot komutlarını gösterir", guild = Object(id = uid))
async def yardım(ctx: Interaction):
    embed = Embed(title="Yardım", description="Yardım komutları", color=0x8a0a01)
    embed.add_field(name="!yardım", value="yardım komutlarını gösterir", inline=False)
    embed.add_field(name="!yak <@Banlanacak kişi>", value="Etiketlenen kişiyi yakar(banlar)", inline=False)
    embed.add_field(name="!kick <@kicklenecek kişi>", value="Etiketlenen kişiyi kickler", inline=False)
    embed.add_field(name="!i <resim ismi>", value="110'dan fazla gif veya resimden seçileni atar. Resim listesi için !i help yazabilirsiniz", inline=False)
    embed.add_field(name="!başvuru <4 formdan birisi>", value="Seçilen başvuru formunu gönderir", inline=False)
    embed.add_field(name="!ada <Adanacak şey>", value="İstediğiniz bir şeyi hayalet vatoza adar", inline=False)
    embed.add_field(name="!pp <@profil fotoğrafını istediğiniz>", value="Yazan kişinin profil fotoğrafını atar", inline=False)
    embed.add_field(name="!ideoloji <istediğiniz ideoloji veya ülke>", value="130 ideoloji arasından seçilen ideolojiye geçerim", inline=False)
    embed.add_field(name="!söz", value="Rastgele bir kişinin sözünü atar", inline=False)
    embed.add_field(name="!propaganda", value="Random propaganda gönderir", inline=False)
    embed.add_field(name="!r <kitap, film, şarkı, oyun, anime veya anime>", value="Seçilen kitap, film, şarkı, oyun, anime veya manga seçeneklerden birisi için öneride bulunur gönderir", inline=False)
    embed.add_field(name="!fok", value="Foka dönüşürüm", inline=False)
    embed.add_field(name="!hoi4tip", value="Hearts of iron 4 için ipucu veririm")
    await ctx.response.send_message(embed=embed)

# gifs


@Bot.command(name = "resim", description = "120'den fazla giften seçileni atar", guild = Object(id = uid))
async def i(ctx: Interaction, args: str):
    if "like" in args:
        await ctx.response.send_message(like)
    if "rage" in args:
        await ctx.response.send_message(rage)
    if "anakuzusu" in args:
        await ctx.response.send_message(anakuzusu)
    if "cry" in args:
        await ctx.response.send_message(cry)
    if "freakout" in args:
        await ctx.response.send_message(freakout)
    if "haa" in args:
        await ctx.response.send_message(haa)
    if "o7konosuba" in args:
        await ctx.response.send_message(o7konosuba)
    if "nomnom" in args:
        await ctx.response.send_message(nomnom)
    if "like2x" in args:
        await ctx.response.send_message(like2x)
    if "shock" in args:
        await ctx.response.send_message(shock)
    if "o7" in args:
        await ctx.response.send_message(o7)
    if "foksax" in args:
        await ctx.response.send_message(foksax)
    if "dwayne" in args:
        await ctx.response.send_message(dwayne)
    if "hatsoff" in args:
        await ctx.response.send_message(hatsoff)
    if "capitalism" in args:
        await ctx.response.send_message(capitalism)
    if "soviet" in args:
        await ctx.response.send_message(soviet)
    if "sikin" in args:
        await ctx.response.send_message(sikin)
    if "susamuru" in args:
        await ctx.response.send_message(susamuru)
    if "fire" in args:
        await ctx.response.send_message(fire)
    if "marcharmy" in args:
        await ctx.response.send_message(marcharmy)
    if "irumadance" in args:
        await ctx.response.send_message(irumadance)
    if "taam" in args:
        await ctx.response.send_message(taam)
    if "stare" in args:
        await ctx.response.send_message(stare)
    if "napim" in args:
        await ctx.response.send_message(napim)
    if "hatayapar" in args:
        await ctx.response.send_message(hatayapar)
    if "nazifokları" in args:
        await ctx.response.send_message(nazifokları)
    if "troll" in args:
        await ctx.response.send_message(troll)
    if "yahudiler" in args:
        await ctx.response.send_message(yahudiler)
    if "balanced" in args:
        await ctx.response.send_message(balanced)
    if "shipbang" in args:
        await ctx.response.send_message(shipbang)
    if "tank" in args:
        await ctx.response.send_message(tank)
    if "degil" in args:
        await ctx.response.send_message(degil)
    if "air" in args:
        await ctx.response.send_message(air)
    if "kimclap" in args:
        await ctx.response.send_message(kimclap)
    if "worry" in args:
        await ctx.response.send_message(worry)
    if "muso" in args:
        await ctx.response.send_message(muso)
    if "sob" in args:
        await ctx.response.send_message(sob)
    if "kannaeat" in args:
        await ctx.response.send_message(kannaeat)
    if "baka" in args:
        await ctx.response.send_message(baka)
    if "triggered" in args:
        await ctx.response.send_message(triggered)
    if "shinobu" in args:
        await ctx.response.send_message(shinobu)
    if "shy" in args:
        await ctx.response.send_message(shy)
    if "bang2" in args:
        await ctx.response.send_message(bang2)
    if "shutup" in args:
        await ctx.response.send_message(shutup)
    if "save" in args:
        await ctx.response.send_message(save)
    if "aah" in args:
        await ctx.response.send_message(aah)
    if "para" in args:
        await ctx.response.send_message(para)
    if "yay" in args:
        await ctx.response.send_message(yay)
    if "anlıyorum" in args:
        await ctx.response.send_message(anlıyorum)
    if "understood" in args:
        await ctx.response.send_message(understood)
    if "igetit" in args:
        await ctx.response.send_message(igetit)
    if "benzin" in args:
        await ctx.response.send_message(benzin)
    if "why" in args:
        await ctx.response.send_message(why)
    if "celebrate" in args:
        await ctx.response.send_message(celebrate)
    if "braintime" in args:
        await ctx.response.send_message(braintime)
    if "drink" in args:
        await ctx.response.send_message(drink)
    if "bb" in args:
        await ctx.response.send_message(bb)
    if "dot" in args:
        await ctx.response.send_message(dot)
    if "confused" in args:
        await ctx.response.send_message(confused)
    if "lenny" in args:
        await ctx.response.send_message(lenny)
    if "bang" in args:
        await ctx.response.send_message(bang)
    if "slap" in args:
        await ctx.response.send_message(slap)
    if "mad" in args:
        await ctx.response.send_message(mad)
    if "sob2" in args:
        await ctx.response.send_message(sob2)
    if "laugh" in args:
        await ctx.response.send_message(laugh)
    if "evilsmile" in args:
        await ctx.response.send_message(evilsmile)
    if "dissaper" in args:
        await ctx.response.send_message(dissaper)
    if "behind" in args:
        await ctx.response.send_message(behind)
    if "like3" in args:
        await ctx.response.send_message(like3)
    if "whatanime" in args:
        await ctx.response.send_message(whatanime)
    if "nomnomnom" in args:
        await ctx.response.send_message(nomnomnom)
    if "bonk" in args:
        await ctx.response.send_message(bonk)
    if "yarra" in args:
        await ctx.response.send_message(yarra)
    if "katon" in args:
        await ctx.response.send_message(katon)
    if "hug" in args:
        await ctx.response.send_message(hug)
    if "hug2" in args:
        await ctx.response.send_message(hug2)
    if "sob3" in args:
        await ctx.response.send_message(sob3)
    if "animechild" in args:
        await ctx.response.send_message(animechild)
    if "narutodance" in args:
        await ctx.response.send_message(narutodance)
    if "darkstare" in args:
        await ctx.response.send_message(darkstare)
    if "think" in args:
        await ctx.response.send_message(think)
    if "point" in args:
        await ctx.response.send_message(point)
    if "bagıs" in args:
        await ctx.response.send_message(bagıs)
    if "stalinpoint" in args:
        await ctx.response.send_message(stalinpoint)
    if "serve" in args:
        await ctx.response.send_message(serve)
    if "waku" in args:
        await ctx.response.send_message(waku)
    if "fail" in args:
        await ctx.response.send_message(fail)
    if "comunazi" in args:
        await ctx.response.send_message(comunazi)
    if "şaak" in args:
        await ctx.response.send_message(şaak)
    if "doom" in args:
        await ctx.response.send_message(doom)
    if "omori" in args:
        await ctx.response.send_message(omori)
    if "papas" in args:
        await ctx.response.send_message(papas)
    if "hans" in args:
        await ctx.response.send_message(hans)
    if "yummy" in args:
        await ctx.response.send_message(yummy)
    if "okay" in args:
        await ctx.response.send_message(okay)
    if "what" in args:
        await ctx.response.send_message(what)
    if "sad" in args:
        await ctx.response.send_message(sad)
    if "gel" in args:
        await ctx.response.send_message(gel)
    if "ekonomi" in args:
        await ctx.response.send_message(ekonomi)
    if "mikasa" in args:
        await ctx.response.send_message(mikasa)
    if "çıldır" in args:
        await ctx.response.send_message(çıldır)
    if "kırk" in args:
        await ctx.response.send_message(kırk)
    if "drink2" in args:
        await ctx.response.send_message(drink2)
    if "fbi" in args:
        await ctx.response.send_message(fbi)
    if "want" in args:
        await ctx.response.send_message(want)
    if "want2" in args:
        await ctx.response.send_message(want2)
    if "tehe" in args:
        await ctx.response.send_message(tehe)
    if "cringe" in args:
        await ctx.response.send_message(cringe)
    if "money" in args:
        await ctx.response.send_message(money)
    if "yay2" in args:
        await ctx.response.send_message(yay2)
    if "nod" in args:
        await ctx.response.send_message(nod)
    if "tobi" in args:
        await ctx.response.send_message(tobi)
    if "yesmaster" in args:
        await ctx.response.send_message(yesmaster)
    if "nope" in args:
        await ctx.response.send_message(nope)


# Bug fix
@Bot.command()
async def aki(ctx: Interaction):
    print("")


@Bot.command()
async def rank(ctx: Interaction):
    print("")

@Bot.command()
async def owo(ctx: Interaction):
    print("")

# ekibe başvuru


@Bot.command(name = "başvuru", description = "4 formdan seçileni gönderiri", guild = Object(id = uid))
async def başvuru(ctx: Interaction, args: str):
    if "mangaçevirmen" in args:
        tr = Embed(
            title="Manga çevirmen başvuru formu",
            description="Daha önce başka bir ekipte çalıştın mı?\n\nBağımsız da olsa deneyimin var mı?\n\nİngilizce seviyen nedir?\n\nEn çok hangi tür mangaları seviyorsun?\n\nİngilizceni değerlendiriniz(A1, A2, B1, B2, C1, C2)\n\nHaftada kaç bölüm çevirebilirsin?\n\nVe bu örnek sayfayı çevirmeni istiyoruz\n\nhttps://drive.google.com/file/d/1_qfW23Wvda94S19U3f4x8eCe6YEqFCug/view?usp=sharing\n\nSon olarak #yeni-gelenlere kanalına bakmayı unutmayın."
        )
        await ctx.response.send_message(embed=tr)
    if "mangaeditör" in args:
        ed = Embed(
            title="Manga editör başvuru formu",
            description="Daha önce başka bir ekipte çalıştın mı?\n\nBağımsız da olsa deneyimin var mı?\n\nHaftada kaç bölüm editleyebilirsin?\n\nPhotoshop seviyene 5 üzerinden puan verebilir misin?\n\nVe bu örnek sayfayı editlemeni istiyoruz\n\nhttps://drive.google.com/file/d/1-B-xLpofKmmyx86_wOuOA4ii-LfG4hb9/view?usp=sharing\n\nSon olarak #yeni-gelenlere kanalına bakmayı unutmayın")
        await ctx.response.send_message(embed=ed)
    if "webçevirmen" in args:
        wtr = Embed(
            title="Webtoon çevirmen başvuru formu",
            description="Daha önce başka bir ekipte çalıştın mı?\n\nBağımsız da olsa deneyimin var mı?\n\nİngilizce seviyen nedir?\n\nEn çok hangi tür webtoonları seviyorsun?\n\nİngilizceni değerlendiriniz(A1, A2, B1, B2, C1, C2)\n\nHaftada kaç bölüm çevirebilirsin?\n\nVe bu örnek sayfayı çevirmeni istiyoruz\nhttps://drive.google.com/drive/folders/11wQIAnl1nSrZSbLDlHFd_CVFvkKazsmZ?usp=sharing\nSon olarak #yeni-gelenlere kanalına bakmayı unutmayın")
        await ctx.response.send_message(embed=wtr)
    if "webeditör" in args:
        wed = Embed(
            title="Webtoon editör başvuru formu",
            description="Daha önce başka bir ekipte çalıştın mı?\n\nBağımsız da olsa deneyimin var mı?\n\nHaftada kaç bölüm editleyebilirsin?\n\nPhotoshop seviyene 5 üzerinden puan verebilir misin?\n\nVe bu örnek sayfayı editlemeni istiyoruz\n\nhttps://drive.google.com/drive/folders/1klKtOSqZDUovb3F9aGfF9NqBLuEVrbEN?usp=sharing\n\nSon olarak #yeni-gelenlere kanalına bakmayı unutmayın"
        )
        await ctx.response.send_message(embed=wed)


# Adak sistemi


@Bot.command(name = "ada", description = "Hayalet Vatoza adağınızı sunar", guild = Object(id = uid))
async def ada(ctx: Interaction, args:str):
    author = str(ctx.ctx.author)
    ad = "adaklar/"+ author +".txt"
    if "temizle" in args:
        os.remove(ad)
        embed = Embed(title="Adağınız başarıyla temizlendi.")
        await ctx.response.send_message(embed=embed)
    if os.path.exists(ad) == True and "temizle" not in args:
        msg = Embed(title="Adağınız kabul edildi")
        await ctx.response.send_message(embed=msg)
        r = open(ad, "r")
        ar = r.read()
        ada = open(str(ad), "w")
        a = str(ar) + ", " + str(args)
        ada.write(a)
    if os.path.exists(ad) == False and "temizle" not in args:
        msg = Embed(title="Adağınız kabul edildi")
        await ctx.response.send_message(embed=msg)
        ada = open(str(ad), "x")
        ada = open(str(ad), "w")
        a = str(args)
        ada.write(a)


@Bot.command(name = "pp", description = "Etiketlenen kişinin profil fotoğrafını gönderir", guild = Object(id = uid))
async def pp(ctx: Interaction, mem: Member):
    await ctx.response.send_message(mem.avatar)


@Bot.command(name = "spp", description = "Profil fotoğrafını gönderir", guild = Object(id = uid))
async def spp(ctx: Interaction):
    icon_url = ctx.guild.icon
    await ctx.response.send_message(f"{icon_url}")


@Bot.command(name = "fok", description = "Bu komut bazı hatalardan dolayı kullanılamamaktadır", guild = Object(id = uid))
async def fok(ctx: Interaction):
    print("")


@Bot.command(name = "vatoz", description = "Bu komut bazı hatalardan dolayı kullanılamamaktadır", guild = Object(id = uid))
async def vatoz(ctx: Interaction):
    print("")

@Bot.command(name = "ideoloji", description = "Vatozun ideolojisini değiştirir", guild = Object(id = uid))
async def ideoloji(ctx: Interaction, ülke: str):
        if "ak4747" in ülke:
            dem = open("vatozlar/ak4747.jpg", 'rb')
            demo = dem.read()
            await client.change_presence(activity=Game(name="Etrafa sikmaca"))
            await client.user.edit(username="Bilge AK-4747 Vatoz", avatar=demo)
            vatoz = "demokrat"
            print(vatoz)
            embed = Embed(title="Bir can karşılığında bir can. Bence mantıklı bir anlaşma")
            await ctx.response.send_message(embed=embed)
        if "almanya" in ülke:
            dem = open("vatozlar/almanya.jpg", 'rb')
            demo = dem.read()
            await client.change_presence(activity=Game(name="Yaşıyor"))
            await client.user.edit(username="Bilge Alman Vatoz", avatar=demo)
            vatoz = "demokrat"
            print(vatoz)
            embed = Embed(title="Alman oldum")
            await ctx.response.send_message(embed=embed)
        if "anarşist" in ülke:
            fas = open("vatozlar/anarşist.jpg", 'rb')
            fasc = fas.read()
            await client.change_presence(activity=Game(name="Otoriteye küfür ediyor"))
            await client.user.edit(username="Bilge Anarşist Vatoz", avatar=fasc)
            vatoz = "anarşist"
            print(vatoz)
            embed = Embed(title="Otoritede ne?")
            await ctx.response.send_message(embed=embed)
        if "anarkoilkel" in ülke:
            ail = open("vatozlar/Anarko-ilkelcilik_vatoz.jpg", 'rb')
            ailk = ail.read()
            await client.change_presence(activity=Game(name="Hayvan avlıyor"))
            await client.user.edit(username="Bilge Anarko-ilkelci Vatoz", avatar=fasc)
            vatoz = "anarko ilkelci"
            print(vatoz)
            embed = Embed(title="Yeni dünya boş asıl olay geçmişte var")
            await ctx.response.send_message(embed=embed)
        if "anarkokapitalist" in ülke:
            fas = open("vatozlar/Anarko-kapitalist_vatoz.jpg", 'rb')
            fasc = fas.read()
            await client.change_presence(activity=Game(name="Tüccarlık yapıyor"))
            await client.user.edit(username="Bilge Anarko Vatoz", avatar=fasc)
            vatoz = "anarko kapitalist"
            print(vatoz)
            embed = Embed(title="Serbest piyasasında tüccarlık yapacağım")
            await ctx.response.send_message(embed=embed)
        if "Avusturya" in ülke:
            dem = open("vatozlar/Avusturya.jpg", 'rb')
            demo = dem.read()
            await client.change_presence(activity=Game(name="Yaşamaya çalışıyor"))
            await client.user.edit(username="Bilge Avusturyalı Vatoz", avatar=demo)
            vatoz = "demokrat"
            print(vatoz)
            embed = Embed(title="Avusturyalı oldum")
            await ctx.response.send_message(embed=embed)
        if "azerbeycan" in ülke:
            dem = open("vatozlar/azerbeycan.jpg", 'rb')
            demo = dem.read()
            await client.change_presence(activity=Game(name="Yaşamaya çalışıyor"))
            await client.user.edit(username="Bilge Azerbeycanlı Vatoz", avatar=demo)
            vatoz = "demokrat"
            print(vatoz)
            embed = Embed(title="Türk oldum")
            await ctx.response.send_message(embed=embed)
        if "Belarus" in ülke:
            dem = open("vatozlar/Belarus.jpg", 'rb')
            demo = dem.read()
            await client.change_presence(activity=Game(name="Yaşamaya çalışıyor"))
            await client.user.edit(username="Bilge Belaruslu Vatoz", avatar=demo)
            vatoz = "demokrat"
            print(vatoz)
            embed = Embed(title="Belaruslu oldum")
            await ctx.response.send_message(embed=embed)
        if "Belçika" in ülke:
            dem = open("vatozlar/Belçika.jpg", 'rb')
            demo = dem.read()
            await client.change_presence(activity=Game(name="Yaşamaya çalışıyor"))
            await client.user.edit(username="Bilge Belçikalı Vatoz", avatar=demo)
            vatoz = "demokrat"
            print(vatoz)
            embed = Embed(title="Belçikalı oldum")
            await ctx.response.send_message(embed=embed)
        if "BosnaHersek" in ülke:
            dem = open("vatozlar/bosna.jpg", 'rb')
            demo = dem.read()
            await client.change_presence(activity=Game(name="Yaşamaya çalışıyor"))
            await client.user.edit(username="Bilge Bosnalı Vatoz", avatar=demo)
            vatoz = "demokrat"
            print(vatoz)
            embed = Embed(title="Bosnalı oldum")
            await ctx.response.send_message(embed=embed)
        if "Bulgaristan" in ülke:
            dem = open("vatozlar/Bulgaristan.jpg", 'rb')
            demo = dem.read()
            await client.change_presence(activity=Game(name="Yaşamaya çalışıyor"))
            await client.user.edit(username="Bilge Bulgar Vatoz", avatar=demo)
            vatoz = "demokrat"
            print(vatoz)
            embed = Embed(title="Bulgar oldum")
            await ctx.response.send_message(embed=embed)
        if "Çek" in ülke:
            dem = open("vatozlar/Çek.jpg", 'rb')
            demo = dem.read()
            await client.change_presence(activity=Game(name="Yaşamaya çalışıyor"))
            await client.user.edit(username="Bilge Çekli Vatoz", avatar=demo)
            vatoz = "demokrat"
            print(vatoz)
            embed = Embed(title="Çekli oldum")
            await ctx.response.send_message(embed=embed)
        if "demokrat" in ülke:
            dem = open("vatozlar/demokrat.jpg", 'rb')
            demo = dem.read()
            await client.change_presence(activity=Game(name="Oy saymaca"))
            await client.user.edit(username="Bilge Demokrat Vatoz", avatar=demo)
            vatoz = "demokrat"
            print(vatoz)
            embed = Embed(title="Herkes istiklalimde eşit özgür olacak")
            await ctx.response.send_message(embed=embed)
        if "Danimarka" in ülke:
            dem = open("vatozlar/denmark.jpg", 'rb')
            demo = dem.read()
            await client.change_presence(activity=Game(name="Yaşamaya çalışıyor"))
            await client.user.edit(username="Bilge Danimarkalı Vatoz", avatar=demo)
            vatoz = "demokrat"
            print(vatoz)
            embed = Embed(title="Danimarkalı oldum")
            await ctx.response.send_message(embed=embed)
        if "ermenistan" in ülke:
            dem = open("vatozlar/ermenistan.jpg", 'rb')
            demo = dem.read()
            await client.change_presence(activity=Game(name="Yaşamaya çalışıyor"))
            await client.user.edit(username="Bilge Eremeni Vatoz", avatar=demo)
            vatoz = "demokrat"
            print(vatoz)
            embed = Embed(title="Ermeni oldum")
            await ctx.response.send_message(embed=embed)
        if "Estonya" in ülke:
            dem = open("vatozlar/estonya.jpg", 'rb')
            demo = dem.read()
            await client.change_presence(activity=Game(name="Yaşamaya çalışıyor"))
            await client.user.edit(username="Bilge Estonyalı Vatoz", avatar=demo)
            vatoz = "demokrat"
            print(vatoz)
            embed = Embed(title="Estonyalı oldum")
            await ctx.response.send_message(embed=embed)
        if "fabrika" in ülke:
            fas = open("vatozlar/fabrika_vatoz.jpg", 'rb')
            fasc = fas.read()
            await client.change_presence(activity=Game(name="Edit yapıyor"))
            await client.user.edit(username="Bilge Fabrika Vatoz", avatar=fasc)
            vatoz = "fabrika"
            print(vatoz)
            embed = Embed(title="İdeolojileri boş verdim ben edit yapacağım")
            await ctx.response.send_message(embed=embed)
        if "faşist" in ülke:
            fas = open("vatozlar/fasist_vatoz.jpg", 'rb')
            fasc = fas.read()
            await client.change_presence(activity=Game(name="Yahudi yakmaca"))
            await client.user.edit(username="Bilge Faşist Vatoz", avatar=fasc)
            vatoz = "faşist"
            embed = Embed(title="Köklerime döndüm")
            await ctx.response.send_message(embed=embed)
        if "finlandiya" in ülke:
            dem = open("vatozlar/finland.jpg", 'rb')
            demo = dem.read()
            await client.change_presence(activity=Game(name="Yaşamaya çalışıyor"))
            await client.user.edit(username="Bilge Finlandiyalı Vatoz", avatar=demo)
            vatoz = "demokrat"
            print(vatoz)
            embed = Embed(title="Finlandiyalı oldum")
            await ctx.response.send_message(embed=embed)
        if "fransa" in ülke:
            dem = open("vatozlar/fransa.jpg", 'rb')
            demo = dem.read()
            await client.change_presence(activity=Game(name="Yaşamaya çalışıyor"))
            await client.user.edit(username="Bilge Fransız Vatoz", avatar=demo)
            vatoz = "demokrat"
            print(vatoz)
            embed = Embed(title="Fransız oldum")
            await ctx.response.send_message(embed=embed)
        if "gürcistan" in ülke:
            dem = open("vatozlar/Gürcistan.jpg", 'rb')
            demo = dem.read()
            await client.change_presence(activity=Game(name="Yaşamaya çalışıyor"))
            await client.user.edit(username="Bilge Gürci Vatoz", avatar=demo)
            vatoz = "demokrat"
            print(vatoz)
            embed = Embed(title="Gürcistanlı oldum")
            await ctx.response.send_message(embed=embed)
        if "hırvatistan" in ülke:
            dem = open("vatozlar/Hırvatistan.jpg", 'rb')
            demo = dem.read()
            await client.change_presence(activity=Game(name="Yaşamaya çalışıyor"))
            await client.user.edit(username="Bilge Hırvat Vatoz", avatar=demo)
            vatoz = "demokrat"
            print(vatoz)
            embed = Embed(title="Hırvat oldum")
            await ctx.response.send_message(embed=embed)
        if "irlanda" in ülke:
            dem = open("vatozlar/İrlanda.jpg", 'rb')
            demo = dem.read()
            await client.change_presence(activity=Game(name="Yaşamaya çalışıyor"))
            await client.user.edit(username="Bilge İrlandalı Vatoz", avatar=demo)
            vatoz = "demokrat"
            print(vatoz)
            embed = Embed(title="İrlandalı oldum")
            await ctx.response.send_message(embed=embed)
        if "İspanya" in ülke:
            dem = open("vatozlar/ispanya.jpg", 'rb')
            demo = dem.read()
            await client.change_presence(activity=Game(name="Yaşamaya çalışıyor"))
            await client.user.edit(username="Bilge İspanyol Vatoz", avatar=demo)
            vatoz = "demokrat"
            print(vatoz)
            embed = Embed(title="İspanyol oldum")
            await ctx.response.send_message(embed=embed)
        if "İtalya" in ülke:
            dem = open("vatozlar/italya.jpg", 'rb')
            demo = dem.read()
            await client.change_presence(activity=Game(name="Yaşamaya çalışıyor"))
            await client.user.edit(username="Bilge İtalyan Vatoz", avatar=demo)
            vatoz = "demokrat"
            print(vatoz)
            embed = Embed(title="İtalyan oldum")
            await ctx.response.send_message(embed=embed)
        if "izlanda" in ülke:
            dem = open("vatozlar/izlanda.jpg", 'rb')
            demo = dem.read()
            await client.change_presence(activity=Game(name="Yaşamaya çalışıyor"))
            await client.user.edit(username="Bilge İzlandalı Vatoz", avatar=demo)
            vatoz = "demokrat"
            print(vatoz)
            embed = Embed(title="İzlandalı oldum")
            await ctx.response.send_message(embed=embed)
        if "karadağ" in ülke:
            dem = open("vatozlar/Karadağ.jpg", 'rb')
            demo = dem.read()
            await client.change_presence(activity=Game(name="Yaşamaya çalışıyor"))
            await client.user.edit(username="Bilge Karadağlı Vatoz", avatar=demo)
            vatoz = "demokrat"
            print(vatoz)
            embed = Embed(title="Karadağlı oldum")
            await ctx.response.send_message(embed=embed)
        if "kazakistan" in ülke:
            dem = open("vatozlar/kazakistan.jpg", 'rb')
            demo = dem.read()
            await client.change_presence(activity=Game(name="Yaşamaya çalışıyor"))
            await client.user.edit(username="Bilge Kazak Vatoz", avatar=demo)
            vatoz = "demokrat"
            print(vatoz)
            embed = Embed(title="Kazak oldum")
            await ctx.response.send_message(embed=embed)
        if "kıbrıs" in ülke:
            dem = open("vatozlar/kıbrıs.jpg", 'rb')
            demo = dem.read()
            await client.change_presence(activity=Game(name="Yaşamaya çalışıyor"))
            await client.user.edit(username="Bilge Kıbrıslı Vatoz", avatar=demo)
            vatoz = "demokrat"
            print(vatoz)
            embed = Embed(title="Kıbrıslı oldum")
            await ctx.response.send_message(embed=embed)
        if "kuma" in ülke:
            fas = open("vatozlar/kuma vatoz.jpg", 'rb')
            fasc = fas.read()
            await client.change_presence(activity=Game(name="Dünyayı kumalıyor"))
            await client.user.edit(username="Bilge Kuma Vatoz", avatar=fasc)
            vatoz = "kuma"
            print(vatoz)
            embed = Embed(title="Kuma kuma kuma bear izleyip geldim")
            await ctx.response.send_message(embed=embed)
        if "kuzey kıbrıs" in ülke:
            dem = open("vatozlar/kuzey-kıbrıs.jpg", 'rb')
            demo = dem.read()
            await client.change_presence(activity=Game(name="Yaşamaya çalışıyor"))
            await client.user.edit(username="Bilge Kuzey kıbrıslı Vatoz", avatar=demo)
            vatoz = "demokrat"
            print(vatoz)
            embed = Embed(title="Kuzey kıbrıslı oldum")
            await ctx.response.send_message(embed=embed)
        if "makedonya" in ülke:
            dem = open("vatozlar/kuzey-makedonya.jpg", 'rb')
            demo = dem.read()
            await client.change_presence(activity=Game(name="Yaşamaya çalışıyor"))
            await client.user.edit(username="Bilge Makedonyalı Vatoz", avatar=demo)
            vatoz = "demokrat"
            print(vatoz)
            embed = Embed(title="Makedonyalı oldum")
            await ctx.response.send_message(embed=embed)
        if "letonya" in ülke:
            dem = open("vatozlar/Latvia.jpg", 'rb')
            demo = dem.read()
            await client.change_presence(activity=Game(name="Yaşamaya çalışıyor"))
            await client.user.edit(username="Bilge Letonyalı Vatoz", avatar=demo)
            vatoz = "demokrat"
            print(vatoz)
            embed = Embed(title="Letonyalı oldum")
            await ctx.response.send_message(embed=embed)
        if "liberteryanist" in ülke:
            fas = open("vatozlar/librteryenist.jpg", 'rb')
            fasc = fas.read()
            await client.change_presence(activity=Game(name="Özgürlüğün dibine vuruyor"))
            await client.user.edit(username="Bilge Liberteryanist Vatoz", avatar=fasc)
            vatoz = "liberteryanist"
            print(vatoz)
            embed = Embed(title="Özgürlük, özgürlük ve daha fazla özgürlük")
            await ctx.response.send_message(embed=embed)
        if "liechtenstein" in ülke:
            dem = open("vatozlar/Liechtenstein.jpg", 'rb')
            demo = dem.read()
            await client.change_presence(activity=Game(name="Yaşamaya çalışıyor"))
            await client.user.edit(username="Bilge Liechtensteinlı Vatoz", avatar=demo)
            vatoz = "demokrat"
            print(vatoz)
            embed = Embed(title="Liechtensteinlı oldum")
            await ctx.response.send_message(embed=embed)
        if "litvanya" in ülke:
            dem = open("vatozlar/lithuania.jpg", 'rb')
            demo = dem.read()
            await client.change_presence(activity=Game(name="Yaşamaya çalışıyor"))
            await client.user.edit(username="Bilge Litvanyalı Vatoz", avatar=demo)
            vatoz = "demokrat"
            print(vatoz)
            embed = Embed(title="Litvanyalı oldum")
            await ctx.response.send_message(embed=embed)
        if "lüksemburg" in ülke:
            dem = open("vatozlar/Lüksemburg.jpg", 'rb')
            demo = dem.read()
            await client.change_presence(activity=Game(name="Yaşamaya çalışıyor"))
            await client.user.edit(username="Bilge Lüksemburglu Vatoz", avatar=demo)
            vatoz = "demokrat"
            print(vatoz)
            embed = Embed(title="Lüksemburglu oldum")
            await ctx.response.send_message(embed=embed)
        if "Macaristan" in ülke:
            dem = open("vatozlar/Macaristan.jpg", 'rb')
            demo = dem.read()
            await client.change_presence(activity=Game(name="Yaşamaya çalışıyor"))
            await client.user.edit(username="Bilge Macar Vatoz", avatar=demo)
            vatoz = "demokrat"
            print(vatoz)
            embed = Embed(title="Macar oldum")
            await ctx.response.send_message(embed=embed)
        if "mao" in ülke:
            fas = open("vatozlar/maocu.jpg", 'rb')
            fasc = fas.read()
            await client.change_presence(activity=Game(name="Kırlarda hazırlanıyor"))
            await client.user.edit(username="Bilge Maocu Vatoz", avatar=fasc)
            vatoz = "maocu"
            print(vatoz)
            embed = Embed(title="马克思主义者认为，只有人们的社会实践，才是人们对于外界认识的真理性的标准。……判定认识或理论之是否真理，不是依主观上觉得如何而定，而是依客观上社会实践的结果如何而定。真理的标准只能是社会的实践。")
            await ctx.response.send_message(embed=embed)
        if "moldova" in ülke:
            dem = open("vatozlar/moldovo.jpg", 'rb')
            demo = dem.read()
            await client.change_presence(activity=Game(name="Yaşamaya çalışıyor"))
            await client.user.edit(username="Bilge Moldovalı Vatoz", avatar=demo)
            vatoz = "demokrat"
            print(vatoz)
            embed = Embed(title="Moldovalı oldum")
            await ctx.response.send_message(embed=embed)
        if "monako" in ülke:
            dem = open("vatozlar/Monaco.jpg", 'rb')
            demo = dem.read()
            await client.change_presence(activity=Game(name="Yaşamaya çalışıyor"))
            await client.user.edit(username="Bilge Monakolu Vatoz", avatar=demo)
            vatoz = "demokrat"
            print(vatoz)
            embed = Embed(title="Monakolu oldum")
            await ctx.response.send_message(embed=embed)
        if "norveç" in ülke:
            dem = open("vatozlar/norway.jpg", 'rb')
            demo = dem.read()
            await client.change_presence(activity=Game(name="Yaşamaya çalışıyor"))
            await client.user.edit(username="Bilge Norveçli Vatoz", avatar=demo)
            vatoz = "demokrat"
            print(vatoz)
            embed = Embed(title="Norveçli oldum")
            await ctx.response.send_message(embed=embed)
        if "onee-san" in ülke:
            dem = open("vatozlar/onee-san.jpg", 'rb')
            demo = dem.read()
            await client.change_presence(activity=Game(name="Minoru-kun'la yaşıyor"))
            await client.user.edit(username="Bilge Onee-san Vatoz", avatar=demo)
            vatoz = "oppai"
            print(vatoz)
            embed = Embed(title="MINORYU-KYUNNNN!!!")
            await ctx.response.send_message(embed=embed)
        if "polonya" in ülke:
            dem = open("vatozlar/poland.jpg", 'rb')
            demo = dem.read()
            await client.change_presence(activity=Game(name="Yaşamaya çalışıyor"))
            await client.user.edit(username="Bilge Polonyalı Vatoz", avatar=demo)
            vatoz = "demokrat"
            print(vatoz)
            embed = Embed(title="Polonyalı oldum")
            await ctx.response.send_message(embed=embed)
        if "radyoaktif" in ülke:
            fas = open("vatozlar/radyoaktif.jpg", 'rb')
            fasc = fas.read()
            await client.change_presence(activity=Game(name="α ışıması yapıyor"))
            await client.user.edit(username="Bilge Radyoaktif Vatoz", avatar=fasc)
            vatoz = "radyoaktif"
            print(vatoz)
            embed = Embed(title="Yanlışlıkla Uranyuma dokundum umarım sıkıntı olmaz")
            await ctx.response.send_message(embed=embed)
        if "romanya" in ülke:
            dem = open("vatozlar/romania.jpg", 'rb')
            demo = dem.read()
            await client.change_presence(activity=Game(name="Yaşamaya çalışıyor"))
            await client.user.edit(username="Bilge Romanyalı Vatoz", avatar=demo)
            vatoz = "demokrat"
            print(vatoz)
            embed = Embed(title="Romanyalı oldum")
            await ctx.response.send_message(embed=embed)
        if "rus" in ülke:
            dem = open("vatozlar/russia.jpg", 'rb')
            demo = dem.read()
            await client.change_presence(activity=Game(name="Yaşamaya çalışıyor"))
            await client.user.edit(username="Bilge Rus Vatoz", avatar=demo)
            vatoz = "demokrat"
            print(vatoz)
            embed = Embed(title="Rus oldum")
            await ctx.response.send_message(embed=embed)
        if "sırbistan" in ülke:
            dem = open("vatozlar/Serbia.jpg", 'rb')
            demo = dem.read()
            await client.change_presence(activity=Game(name="Yaşamaya çalışıyor"))
            await client.user.edit(username="Bilge Sırp Vatoz", avatar=demo)
            vatoz = "demokrat"
            print(vatoz)
            embed = Embed(title="Sırp oldum")
            await ctx.response.send_message(embed=embed)
        if "slovakya" in ülke:
            dem = open("vatozlar/slovakia.jpg", 'rb')
            demo = dem.read()
            await client.change_presence(activity=Game(name="Yaşamaya çalışıyor"))
            await client.user.edit(username="Bilge Slovakyalı Vatoz", avatar=demo)
            vatoz = "demokrat"
            print(vatoz)
            embed = Embed(title="Slovakyalı oldum")
            await ctx.response.send_message(embed=embed)
        if "slovenya" in ülke:
            dem = open("vatozlar/slovenia.jpg", 'rb')
            demo = dem.read()
            await client.change_presence(activity=Game(name="Yaşamaya çalışıyor"))
            await client.user.edit(username="Bilge Slovenyalı Vatoz", avatar=demo)
            vatoz = "demokrat"
            print(vatoz)
            embed = Embed(title="Slovenyalı oldum")
            await ctx.response.send_message(embed=embed)
        if "stalin" in ülke:
            dem = open("vatozlar/Stalin.jpg", 'rb')
            demo = dem.read()
            await client.change_presence(activity=Game(name="Yaşamaya çalışıyor"))
            await client.user.edit(username="Bilge Stalin Vatoz", avatar=demo)
            vatoz = "demokrat"
            print(vatoz)
            embed = Embed(title="Россия - священная наша держава")
            await ctx.response.send_message(embed=embed)
        if "isveç" in ülke:
            dem = open("vatozlar/sweden.jpg", 'rb')
            demo = dem.read()
            await client.change_presence(activity=Game(name="Yaşamaya çalışıyor"))
            await client.user.edit(username="Bilge İsveçli Vatoz", avatar=demo)
            vatoz = "demokrat"
            print(vatoz)
            embed = Embed(title="İsveçli oldum")
            await ctx.response.send_message(embed=embed)
        if "isviçre" in ülke:
            dem = open("vatozlar/switzerland.jpg", 'rb')
            demo = dem.read()
            await client.change_presence(activity=Game(name="Yaşamaya çalışıyor"))
            await client.user.edit(username="Bilge İsviçreli Vatoz", avatar=demo)
            vatoz = "demokrat"
            print(vatoz)
            embed = Embed(title="İsviçreli oldum")
            await ctx.response.send_message(embed=embed)
        if "turan" in ülke:
            fas = open("vatozlar/turancı.jpg", 'rb')
            fasc = fas.read()
            await client.change_presence(activity=Game(name="Haritayı açık maviye boyuyor"))
            await client.user.edit(username="Bilge Turancı Vatoz", avatar=fasc)
            vatoz = "turancı"
            print(vatoz)
            embed = Embed(title="Türkler üstün ırktır ve ben de görevim olan cihan fethini gerçekleştireceğim")
            await ctx.response.send_message(embed=embed)
        if "türk" in ülke:
            fas = open("vatozlar/Türkiye.jpg", 'rb')
            fasc = fas.read()
            await client.change_presence(activity=Game(name="Yaşayamıyor"))
            await client.user.edit(username="Bilge Türk Vatoz", avatar=fasc)
            vatoz = "turancı"
            print(vatoz)
            embed = Embed(title="Ne mutlu Türküm diyene!")
            await ctx.response.send_message(embed=embed)
        if "ukrayna" in ülke:
            dem = open("vatozlar/ukrayna.jpg", 'rb')
            demo = dem.read()
            await client.change_presence(activity=Game(name="Yaşamaya çalışıyor"))
            await client.user.edit(username="Bilge Ukraynalı Vatoz", avatar=demo)
            vatoz = "demokrat"
            print(vatoz)
            embed = Embed(title="Ukraynalı oldum")
            await ctx.response.send_message(embed=embed)
        if "İngiltere" in ülke:
            dem = open("vatozlar/Unitend-kingdom.jpg", 'rb')
            demo = dem.read()
            await client.change_presence(activity=Game(name="Yaşamaya çalışıyor"))
            await client.user.edit(username="Bilge İngiliz Vatoz", avatar=demo)
            vatoz = "demokrat"
            print(vatoz)
            embed = Embed(title="İngiliz oldum")
            await ctx.response.send_message(embed=embed)
        if "yunanistan" in ülke:
            dem = open("vatozlar/yunanistan.jpg", 'rb')
            demo = dem.read()
            await client.change_presence(activity=Game(name="Yaşamaya çalışıyor"))
            await client.user.edit(username="Bilge Yunan Vatoz", avatar=demo)
            vatoz = "demokrat"
            print(vatoz)
            embed = Embed(title="Yunan oldum")
            await ctx.response.send_message(embed=embed)
        if "afganistan" in ülke:
            dem = open("vatozlar/asya/afganistan.jpg", 'rb')
            demo = dem.read()
            await client.change_presence(activity=Game(name="Yaşamaya çalışıyor"))
            await client.user.edit(username="Bilge Afgan Vatoz", avatar=demo)
            vatoz = "demokrat"
            print(vatoz)
            embed = Embed(title="Afgan oldum")
            await ctx.response.send_message(embed=embed)
        if "bahreyn" in ülke:
            dem = open("vatozlar/asya/bahreyn.jpg", 'rb')
            demo = dem.read()
            await client.change_presence(activity=Game(name="Yaşamaya çalışıyor"))
            await client.user.edit(username="Bilge Bahreynli Vatoz", avatar=demo)
            vatoz = "demokrat"
            print(vatoz)
            embed = Embed(title="Bahreynli oldum")
            await ctx.response.send_message(embed=embed)
        if "bangladeş" in ülke:
            dem = open("vatozlar/asya/bangladeş.jpg", 'rb')
            demo = dem.read()
            await client.change_presence(activity=Game(name="Yaşamaya çalışıyor"))
            await client.user.edit(username="Bilge Bangladeşli Vatoz", avatar=demo)
            vatoz = "demokrat"
            print(vatoz)
            embed = Embed(title="Bangladeşli oldum")
            await ctx.response.send_message(embed=embed)
        if "bae" in ülke:
            dem = open("vatozlar/asya/Birleşik arap emirliği.jpg", 'rb')
            demo = dem.read()
            await client.change_presence(activity=Game(name="Yaşamaya çalışıyor"))
            await client.user.edit(username="Cahil Arap Vatoz", avatar=demo)
            vatoz = "demokrat"
            print(vatoz)
            embed = Embed(title="Arap oldum")
            await ctx.response.send_message(embed=embed)
        if "brunei" in ülke:
            dem = open("vatozlar/asya/brunei.jpg", 'rb')
            demo = dem.read()
            await client.change_presence(activity=Game(name="Yaşamaya çalışıyor"))
            await client.user.edit(username="Bilge Bruneyli Vatoz", avatar=demo)
            vatoz = "demokrat"
            print(vatoz)
            embed = Embed(title="Bruneyli oldum")
            await ctx.response.send_message(embed=embed)
        if "butan" in ülke:
            dem = open("vatozlar/asya/butan.jpg", 'rb')
            demo = dem.read()
            await client.change_presence(activity=Game(name="Yaşamaya çalışıyor"))
            await client.user.edit(username="Bilge Butanlı Vatoz", avatar=demo)
            vatoz = "demokrat"
            print(vatoz)
            embed = Embed(title="Butanlı oldum")
            await ctx.response.send_message(embed=embed)
        if "çin" in ülke:
            dem = open("vatozlar/asya/çin.jpg", 'rb')
            demo = dem.read()
            await client.change_presence(activity=Game(name="Yaşamaya çalışıyor"))
            await client.user.edit(username="Bilge Çinli Vatoz", avatar=demo)
            vatoz = "sosyalist"
            print(vatoz)
            embed = Embed(title="近前看其詳上寫着秦香蓮那三十二歲 那狀告當朝驸馬郎")
            await ctx.response.send_message(embed=embed)
        if "timor" in ülke:
            dem = open("vatozlar/asya/doğu timor.jpg", 'rb')
            demo = dem.read()
            await client.change_presence(activity=Game(name="Yaşamaya çalışıyor"))
            await client.user.edit(username="Bilge Timorlu Vatoz", avatar=demo)
            vatoz = "demokrat"
            print(vatoz)
            embed = Embed(title="Timorlu oldum")
            await ctx.response.send_message(embed=embed)
        if "endonezya" in ülke:
            dem = open("vatozlar/asya/endonezya.jpg", 'rb')
            demo = dem.read()
            await client.change_presence(activity=Game(name="Yaşamaya çalışıyor"))
            await client.user.edit(username="Orospu Endonezyalı Vatoz", avatar=demo)
            vatoz = "demokrat"
            print(vatoz)
            embed = Embed(title="Endonezyalı oldum")
            await ctx.response.send_message(embed=embed)
        if "filipinler" in ülke:
            dem = open("vatozlar/asya/filipinler.jpg", 'rb')
            demo = dem.read()
            await client.change_presence(activity=Game(name="Yaşamaya çalışıyor"))
            await client.user.edit(username="Bilge Filipinli Vatoz", avatar=demo)
            vatoz = "demokrat"
            print(vatoz)
            embed = Embed(title="Filipinli oldum")
            await ctx.response.send_message(embed=embed)
        if "güneykore" in ülke:
            dem = open("vatozlar/asya/güney kore.jpg", 'rb')
            demo = dem.read()
            await client.change_presence(activity=Game(name="Yaşamaya çalışıyor"))
            await client.user.edit(username="Bilge Koreli Vatoz", avatar=demo)
            vatoz = "demokrat"
            print(vatoz)
            embed = Embed(title="Koreli oldum")
            await ctx.response.send_message(embed=embed)
        if "hindistan" in ülke:
            dem = open("vatozlar/asya/Hindistan.jpg", 'rb')
            demo = dem.read()
            await client.change_presence(activity=Game(name="Yaşamaya çalışıyor"))
            await client.user.edit(username="Bilge Hintli Vatoz", avatar=demo)
            vatoz = "demokrat"
            print(vatoz)
            embed = Embed(title="Hintli oldum")
            await ctx.response.send_message(embed=embed)
        if "hong-kong" in ülke:
            dem = open("vatozlar/asya/hong-kong.jpg", 'rb')
            demo = dem.read()
            await client.change_presence(activity=Game(name="Yaşamaya çalışıyor"))
            await client.user.edit(username="Bilge Hong-konglu Vatoz", avatar=demo)
            vatoz = "demokrat"
            print(vatoz)
            embed = Embed(title="Hong-konglu oldum")
            await ctx.response.send_message(embed=embed)
        if "ırak" in ülke:
            dem = open("vatozlar/asya/ırak.jpg", 'rb')
            demo = dem.read()
            await client.change_presence(activity=Game(name="Yaşamaya çalışıyor"))
            await client.user.edit(username="Cahil Iraklı Vatoz", avatar=demo)
            vatoz = "demokrat"
            print(vatoz)
            embed = Embed(title="أصبحت عراقيا")
            await ctx.response.send_message(embed=embed)
        if "iran" in ülke:
            dem = open("vatozlar/asya/İran.jpg", 'rb')
            demo = dem.read()
            await client.change_presence(activity=Game(name="Yaşamaya çalışıyor"))
            await client.user.edit(username="Cahil İranlı Vatoz", avatar=demo)
            vatoz = "demokrat"
            print(vatoz)
            embed = Embed(title="أصبحت إيرانيًا")
            await ctx.response.send_message(embed=embed)
        if "israil" in ülke:
            dem = open("vatozlar/asya/israil.jpg", 'rb')
            demo = dem.read()
            await client.change_presence(activity=Game(name="Yaşamaya çalışıyor"))
            await client.user.edit(username="Bilge İsrailli Vatoz", avatar=demo)
            vatoz = "demokrat"
            print(vatoz)
            embed = Embed(title="İsrailli oldum")
            await ctx.response.send_message(embed=embed)
        if "japonya" in ülke:
            dem = open("vatozlar/asya/Japonya.jpg", 'rb')
            demo = dem.read()
            await client.change_presence(activity=Game(name="Yaşıyor"))
            await client.user.edit(username="Ultra Bilge Japon Vatoz", avatar=demo)
            vatoz = "demokrat"
            print(vatoz)
            embed = Embed(title="日本人になった")
            await ctx.response.send_message(embed=embed)
        if "kamboçya" in ülke:
            dem = open("vatozlar/asya/kamboçya.jpg", 'rb')
            demo = dem.read()
            await client.change_presence(activity=Game(name="Yaşamaya çalışıyor"))
            await client.user.edit(username="Bilge Kmer Vatoz", avatar=demo)
            vatoz = "demokrat"
            print(vatoz)
            embed = Embed(title="Kmer oldum")
            await ctx.response.send_message(embed=embed)
        if "katar" in ülke:
            dem = open("vatozlar/asya/Katar.jpg", 'rb')
            demo = dem.read()
            await client.change_presence(activity=Game(name="Yaşamaya çalışıyor"))
            await client.user.edit(username="Zengin Katar Vatoz", avatar=demo)
            vatoz = "demokrat"
            print(vatoz)
            embed = Embed(title="Katarlı oldum")
            await ctx.response.send_message(embed=embed)
        if "kırgızistan" in ülke:
            dem = open("vatozlar/asya/Kırgızistan.jpg", 'rb')
            demo = dem.read()
            await client.change_presence(activity=Game(name="Yaşamaya çalışıyor"))
            await client.user.edit(username="Bilge Kırgız Vatoz", avatar=demo)
            vatoz = "demokrat"
            print(vatoz)
            embed = Embed(title="Kırgız oldum")
            await ctx.response.send_message(embed=embed)
        if "kuveyt" in ülke:
            dem = open("vatozlar/asya/kuveyt.jpg", 'rb')
            demo = dem.read()
            await client.change_presence(activity=Game(name="Yaşamaya çalışıyor"))
            await client.user.edit(username="Bilge Kuveytli Vatoz", avatar=demo)
            vatoz = "demokrat"
            print(vatoz)
            embed = Embed(title="Kuveytli oldum")
            await ctx.response.send_message(embed=embed)
        if "kuzey-kore" in ülke:
            dem = open("vatozlar/asya/kuzey kore.jpg", 'rb')
            demo = dem.read()
            await client.change_presence(activity=Game(name="Yaşamaya çalışıyor"))
            await client.user.edit(username="Bilge Kuzey Koreli Vatoz", avatar=demo)
            vatoz = "demokrat"
            print(vatoz)
            embed = Embed(title="Kuzey Koreli oldum")
            await ctx.response.send_message(embed=embed)
        if "laos" in ülke:
            dem = open("vatozlar/asya/Laos.jpg", 'rb')
            demo = dem.read()
            await client.change_presence(activity=Game(name="Yaşamaya çalışıyor"))
            await client.user.edit(username="Bilge Laoslu Vatoz", avatar=demo)
            vatoz = "demokrat"
            print(vatoz)
            embed = Embed(title="Laoslu oldum")
            await ctx.response.send_message(embed=embed)
        if "lübnan" in ülke:
            dem = open("vatozlar/asya/Lübnan.jpg", 'rb')
            demo = dem.read()
            await client.change_presence(activity=Game(name="Yaşamaya çalışıyor"))
            await client.user.edit(username="Bilge Lübnanlı Vatoz", avatar=demo)
            vatoz = "demokrat"
            print(vatoz)
            embed = Embed(title="Lübnanlı oldum")
            await ctx.response.send_message(embed=embed)
        if "maldivler" in ülke:
            dem = open("vatozlar/asya/Maldivler.jpg", 'rb')
            demo = dem.read()
            await client.change_presence(activity=Game(name="Yaşamaya çalışıyor"))
            await client.user.edit(username="Bilge Maldivli Vatoz", avatar=demo)
            vatoz = "demokrat"
            print(vatoz)
            embed = Embed(title="Maldivli oldum")
            await ctx.response.send_message(embed=embed)
        if "malezya" in ülke:
            dem = open("vatozlar/asya/malezya.jpg", 'rb')
            demo = dem.read()
            await client.change_presence(activity=Game(name="Yaşamaya çalışıyor"))
            await client.user.edit(username="Bilge Malezyalı Vatoz", avatar=demo)
            vatoz = "demokrat"
            print(vatoz)
            embed = Embed(title="Malezyalı oldum")
            await ctx.response.send_message(embed=embed)
        if "mısır" in ülke:
            dem = open("vatozlar/asya/mısır.jpg", 'rb')
            demo = dem.read()
            await client.change_presence(activity=Game(name="Yaşamaya çalışıyor"))
            await client.user.edit(username="Bilge Mısırlı Vatoz", avatar=demo)
            vatoz = "demokrat"
            print(vatoz)
            embed = Embed(title="Mısırlı oldum")
            await ctx.response.send_message(embed=embed)
        if "moğol" in ülke:
            dem = open("vatozlar/asya/moğolistan.jpg", 'rb')
            demo = dem.read()
            await client.change_presence(activity=Game(name="Yaşamaya çalışıyor"))
            await client.user.edit(username="Bilge Moğol Vatoz", avatar=demo)
            vatoz = "demokrat"
            print(vatoz)
            embed = Embed(title="Moğol oldum")
            await ctx.response.send_message(embed=embed)
        if "myanmar" in ülke:
            dem = open("vatozlar/asya/Myanmar.jpg", 'rb')
            demo = dem.read()
            await client.change_presence(activity=Game(name="Yaşamaya çalışıyor"))
            await client.user.edit(username="Bilge Burmalı Vatoz", avatar=demo)
            vatoz = "demokrat"
            print(vatoz)
            embed = Embed(title="Burmalı oldum")
            await ctx.response.send_message(embed=embed)
        if "nepal" in ülke:
            dem = open("vatozlar/asya/nepal.jpg", 'rb')
            demo = dem.read()
            await client.change_presence(activity=Game(name="Yaşamaya çalışıyor"))
            await client.user.edit(username="Bilge Nepalli Vatoz", avatar=demo)
            vatoz = "demokrat"
            print(vatoz)
            embed = Embed(title="Nepalli oldum")
            await ctx.response.send_message(embed=embed)
        if "oman" in ülke:
            dem = open("vatozlar/asya/oman.jpg", 'rb')
            demo = dem.read()
            await client.change_presence(activity=Game(name="Yaşamaya çalışıyor"))
            await client.user.edit(username="Cahil Omanlı Vatoz", avatar=demo)
            vatoz = "demokrat"
            print(vatoz)
            embed = Embed(title="Omanlı oldum")
            await ctx.response.send_message(embed=embed)
        if "özbekistan" in ülke:
            dem = open("vatozlar/asya/özbekistan.jpg", 'rb')
            demo = dem.read()
            await client.change_presence(activity=Game(name="Yaşamaya çalışıyor"))
            await client.user.edit(username="Bilge Türk Vatoz", avatar=demo)
            vatoz = "demokrat"
            print(vatoz)
            embed = Embed(title="Özbek, Türkmen, Uygur, Tatar, Azer bir boydur \nKarakalpak, Kırgız, Kazak bunlar bir soydur")
            await ctx.response.send_message(embed=embed)
        if "pakistan" in ülke:
            dem = open("vatozlar/asya/pakistan.jpg", 'rb')
            demo = dem.read()
            await client.change_presence(activity=Game(name="Yaşamaya çalışıyor"))
            await client.user.edit(username="Bilge Pakistanlı Vatoz", avatar=demo)
            vatoz = "demokrat"
            print(vatoz)
            embed = Embed(title="Pakistanlı oldum")
            await ctx.response.send_message(embed=embed)
        if "singapur" in ülke:
            dem = open("vatozlar/asya/singapur.jpg", 'rb')
            demo = dem.read()
            await client.change_presence(activity=Game(name="Yaşamaya çalışıyor"))
            await client.user.edit(username="Bilge Singapurlu Vatoz", avatar=demo)
            vatoz = "demokrat"
            print(vatoz)
            embed = Embed(title="Singapurlu oldum")
            await ctx.response.send_message(embed=embed)
        if "srilanka" in ülke:
            dem = open("vatozlar/asya/sri lanka.jpg", 'rb')
            demo = dem.read()
            await client.change_presence(activity=Game(name="Yaşamaya çalışıyor"))
            await client.user.edit(username="Bilge Sri Lanka Vatoz", avatar=demo)
            vatoz = "demokrat"
            print(vatoz)
            embed = Embed(title="Sri Lankalı oldum")
            await ctx.response.send_message(embed=embed)
        if "suriye" in ülke:
            dem = open("vatozlar/asya/suriye.jpg", 'rb')
            demo = dem.read()
            await client.change_presence(activity=Game(name="Yaşamaya çalışıyor"))
            await client.user.edit(username="Cahil Suriyeli Vatoz", avatar=demo)
            vatoz = "demokrat"
            print(vatoz)
            embed = Embed(title="أصبحت سوريًا")
            await ctx.response.send_message(embed=embed)
        if "suudi" in ülke:
            dem = open("vatozlar/asya/suudi-america.jpg", 'rb')
            demo = dem.read()
            await client.change_presence(activity=Game(name="Yaşamaya çalışıyor"))
            await client.user.edit(username="Cahil Suudi Vatoz", avatar=demo)
            vatoz = "demokrat"
            print(vatoz)
            embed = Embed(title="أصبحت عربيا")
            await ctx.response.send_message(embed=embed)
        if "tacikistan" in ülke:
            dem = open("vatozlar/asya/tacikistan.jpg", 'rb')
            demo = dem.read()
            await client.change_presence(activity=Game(name="Yaşamaya çalışıyor"))
            await client.user.edit(username="Bilge Tacik Vatoz", avatar=demo)
            vatoz = "demokrat"
            print(vatoz)
            embed = Embed(title="Tacik oldum")
            await ctx.response.send_message(embed=embed)
        if "tayland" in ülke:
            dem = open("vatozlar/asya/tayland.jpg", 'rb')
            demo = dem.read()
            await client.change_presence(activity=Game(name="Yaşamaya çalışıyor"))
            await client.user.edit(username="Bilge Taylandlı Vatoz", avatar=demo)
            vatoz = "demokrat"
            print(vatoz)
            embed = Embed(title="Taylandlı oldum")
            await ctx.response.send_message(embed=embed)
        if "tayvan" in ülke:
            dem = open("vatozlar/asya/tayvan.jpg", 'rb')
            demo = dem.read()
            await client.change_presence(activity=Game(name="Yaşamaya çalışıyor"))
            await client.user.edit(username="Bilge Tayvanlı Vatoz", avatar=demo)
            vatoz = "demokrat"
            print(vatoz)
            embed = Embed(title="Tayvanlı oldum")
            await ctx.response.send_message(embed=embed)
        if "türkmenistan" in ülke:
            dem = open("vatozlar/asya/türkmenistan.jpg", 'rb')
            demo = dem.read()
            await client.change_presence(activity=Game(name="Yaşamaya çalışıyor"))
            await client.user.edit(username="Bilge Türk Vatoz", avatar=demo)
            vatoz = "demokrat"
            print(vatoz)
            embed = Embed(title="Özbek, Türkmen, Uygur, Tatar, Azer bir boydur\nKarakalpak, Kırgız, Kazak bunlar bir soydur")
            await ctx.response.send_message(embed=embed)
        if "ürdün" in ülke:
            dem = open("vatozlar/asya/ürdün.jpg", 'rb')
            demo = dem.read()
            await client.change_presence(activity=Game(name="Yaşamaya çalışıyor"))
            await client.user.edit(username="Cahil Ürdünlü Vatoz", avatar=demo)
            vatoz = "demokrat"
            print(vatoz)
            embed = Embed(title="Arap oldum")
            await ctx.response.send_message(embed=embed)
        if "vietnam" in ülke:
            dem = open("vatozlar/asya/Vietnam.jpg", 'rb')
            demo = dem.read()
            await client.change_presence(activity=Game(name="Yaşamaya çalışıyor"))
            await client.user.edit(username="Bilge Vietnam Vatoz", avatar=demo)
            vatoz = "demokrat"
            print(vatoz)
            embed = Embed(title="Vietnamlı oldum")
            await ctx.response.send_message(embed=embed)
        if "yemen" in ülke:
            dem = open("vatozlar/asya/yemen.jpg", 'rb')
            demo = dem.read()
            await client.change_presence(activity=Game(name="Yaşamaya çalışıyor"))
            await client.user.edit(username="Bilge Yemenli Vatoz", avatar=demo)
            vatoz = "demokrat"
            print(vatoz)
            embed = Embed(title="Yemenli oldum")
            await ctx.response.send_message(embed=embed)


# Söz

@Bot.command(name = "söz", description = "Random olarak önemli bir kişin sözünü gönderir", guild = Object(id = uid))
async def söz(ctx: Interaction):
    l = random.randint(1, 8)
    if l == 1:
        Hitlerlist = [Hitler1,Hitler2,Hitler3, Hitler4, Hitler5, Hitler6, Hitler7, Hitler8, Hitler9, Hitler10, Hitler11, Hitler12, Hitler13, Hitler14, Hitler15, Hitler16, Hitler17, Hitler18, Hitler19, Hitler20, Hitler21, Hitler22, Hitler23, Hitler24, Hitler25, Hitler26, Hitler27, Hitler28, Hitler29, Hitler30, Hitler31, Hitler32, Hitler33, Hitler34, Hitler35, Hitler36, Hitler37, Hitler38, Hitler39, Hitler40, Hitler41, Hitler42, Hitler43, Hitler44, Hitler45, Hitler46, Hitler47, Hitler48, Hitler49, Hitler50, Hitler51, Hitler52, Hitler53, Hitler54, Hitler55, Hitler56, Hitler57, Hitler58, Hitler59, Hitler60, Hitler61, Hitler62, Hitler63, Hitler64, Hitler65, Hitler66, Hitler67, Hitler68, Hitler69, Hitler70, Hitler71, Hitler72, Hitler73, Hitler74, Hitler75, Hitler76, Hitler77, Hitler78, Hitler79, Hitler80, Hitler81, Hitler82, Hitler83, Hitler84, Hitler85, Hitler86, Hitler87, Hitler88, Hitler89, Hitler90, Hitler91, Hitler92, Hitler93, Hitler94, Hitler95, Hitler96, Hitler97, Hitler98, Hitler99, Hitler100, Hitler101, Hitler102, Hitler103, Hitler104, Hitler105, Hitler106, Hitler107, Hitler108, Hitler109, Hitler110, Hitler111, Hitler112, Hitler113, Hitler114, Hitler115, Hitler116, Hitler117, Hitler118, Hitler119, Hitler120, Hitler121, Hitler122, Hitler123, Hitler124, Hitler125, Hitler126, Hitler127, Hitler128, Hitler129, Hitler130, Hitler131, Hitler132, Hitler133, Hitler134, Hitler135, Hitler136, Hitler137, Hitler138, Hitler139, Hitler140, Hitler141, Hitler142, Hitler143, Hitler144, Hitler145, Hitler146, Hitler147, Hitler148, Hitler149, Hitler150, Hitler151, Hitler152, Hitler153, Hitler154, Hitler155, Hitler156, Hitler157, Hitler158, Hitler159, Hitler160, Hitler161, Hitler162, Hitler163, Hitler164, Hitler165, Hitler166, Hitler167, Hitler168, Hitler169, Hitler170, Hitler171, Hitler172, Hitler173, Hitler174, Hitler175, Hitler176, Hitler177, Hitler178, Hitler179, Hitler180, Hitler181, Hitler182, Hitler183, Hitler184, Hitler185, Hitler186, Hitler187, Hitler188, Hitler189, Hitler190, Hitler191, Hitler192, Hitler193, Hitler194, Hitler195, Hitler196, Hitler197, Hitler198, Hitler199, Hitler200, Hitler201, Hitler202, Hitler203, Hitler204, Hitler205, Hitler206, Hitler207, Hitler208, Hitler209, Hitler210, Hitler211, Hitler212, Hitler213, Hitler214, Hitler215, Hitler216, Hitler217, Hitler218, Hitler219, Hitler220, Hitler221, Hitler222, Hitler223, Hitler224, Hitler225, Hitler226, Hitler227, Hitler228, Hitler229, Hitler230, Hitler231, Hitler232, Hitler233, Hitler234, Hitler235, Hitler236, Hitler237, Hitler238, Hitler239, Hitler240, Hitler241, Hitler242, Hitler243, Hitler244, Hitler245, Hitler246, Hitler247, Hitler248, Hitler249, Hitler250, Hitler251, Hitler252, Hitler253, Hitler254, Hitler255, Hitler256, Hitler257]
        f = random.choice(Hitlerlist)
        embed = Embed(title="Hitler derki", description=f)
        await ctx.response.send_message(embed=embed)
    if l == 2:
        Ataturklist = [Ataturk1, Ataturk2, Ataturk3, Ataturk4, Ataturk5, Ataturk6, Ataturk7, Ataturk8, Ataturk9, Ataturk10, Ataturk11, Ataturk12, Ataturk13, Ataturk14, Ataturk15, Ataturk16, Ataturk17, Ataturk18, Ataturk19, Ataturk20, Ataturk21, Ataturk22, Ataturk23, Ataturk24, Ataturk25, Ataturk26, Ataturk27, Ataturk28, Ataturk29, Ataturk30, Ataturk31, Ataturk32, Ataturk33, Ataturk34, Ataturk35, Ataturk36, Ataturk37, Ataturk38, Ataturk39, Ataturk40, Ataturk41, Ataturk42, Ataturk43, Ataturk44, Ataturk45, Ataturk46, Ataturk47, Ataturk48, Ataturk49, Ataturk50, Ataturk51, Ataturk52, Ataturk53, Ataturk54, Ataturk55, Ataturk56, Ataturk57, Ataturk58, Ataturk59, Ataturk60, Ataturk61, Ataturk62, Ataturk63, Ataturk64, Ataturk65, Ataturk66, Ataturk67, Ataturk68, Ataturk69, Ataturk70, Ataturk71, Ataturk72, Ataturk73, Ataturk74, Ataturk75, Ataturk76, Ataturk77, Ataturk78, Ataturk79, Ataturk80, Ataturk81, Ataturk82, Ataturk83, Ataturk84, Ataturk85, Ataturk86, Ataturk87, Ataturk88, Ataturk89, Ataturk90, Ataturk91, Ataturk92, Ataturk93, Ataturk94, Ataturk95, Ataturk96, Ataturk97, Ataturk98, Ataturk99, Ataturk100, Ataturk101, Ataturk102, Ataturk103, Ataturk104, Ataturk105, Ataturk106, Ataturk107, Ataturk108, Ataturk109, Ataturk110, Ataturk111, Ataturk112, Ataturk113, Ataturk114, Ataturk115, Ataturk116, Ataturk117, Ataturk118, Ataturk119, Ataturk120, Ataturk121, Ataturk122, Ataturk123, Ataturk124, Ataturk125, Ataturk126, Ataturk127, Ataturk128, Ataturk129, Ataturk130, Ataturk131, Ataturk132, Ataturk133, Ataturk134, Ataturk135, Ataturk136, Ataturk137, Ataturk138, Ataturk139, Ataturk140, Ataturk141, Ataturk142, Ataturk143, Ataturk144, Ataturk145, Ataturk146, Ataturk147, Ataturk148, Ataturk149, Ataturk150, Ataturk151, Ataturk152, Ataturk153, Ataturk154, Ataturk155, Ataturk156, Ataturk157, Ataturk158, Ataturk159, Ataturk160, Ataturk161, Ataturk162, Ataturk163, Ataturk164, Ataturk165, Ataturk166, Ataturk167, Ataturk168, Ataturk169, Ataturk170, Ataturk171, Ataturk172, Ataturk173, Ataturk174, Ataturk175, Ataturk176, Ataturk177, Ataturk178, Ataturk179, Ataturk180, Ataturk181, Ataturk182, Ataturk183, Ataturk184, Ataturk185, Ataturk186, Ataturk187]
        f = random.choice(Ataturklist)
        embed = Embed(title="Atatürk derki", description=f)
        await ctx.response.send_message(embed=embed)
    if l == 3:
        Leninlist = [Lenin1, Lenin2, Lenin3, Lenin4, Lenin5, Lenin6, Lenin7, Lenin8, Lenin9, Lenin10, Lenin11, Lenin12, Lenin13, Lenin14, Lenin15, Lenin16, Lenin17, Lenin18, Lenin19, Lenin20, Lenin21]
        f = random.choice(Leninlist)
        embed = Embed(title="Lenin derki", description=f)
        await ctx.response.send_message(embed=embed)
    if l == 4:
        Stalinlist = [Stalin1, Stalin2, Stalin3, Stalin4, Stalin5, Stalin6, Stalin7, Stalin8, Stalin9, Stalin10, Stalin11, Stalin12, Stalin13, Stalin14, Stalin15, Stalin16, Stalin17, Stalin18, Stalin19, Stalin20, Stalin21, Stalin22, Stalin23, Stalin24, Stalin25]
        f = random.choice(Stalinlist)
        embed = Embed(title="Stalin derki", description=f)
        await ctx.response.send_message(embed=embed)
    if l == 5:
        Cengizlist = [CengizHan1, CengizHan2, CengizHan3, CengizHan4, CengizHan5, CengizHan6, CengizHan7, CengizHan8, CengizHan9]
        f = random.choice(Cengizlist)
        embed = Embed(title="Cengiz Han derki", description=f)
        await ctx.response.send_message(embed=embed)
    if l == 6:
        CelalŞengörlist = [Celal1, Celal2, Celal3, Celal4, Celal5, Celal6, Celal7, Celal8, Celal9, Celal10, Celal11, Celal12, Celal13, Celal14, Celal15, Celal16, Celal17, Celal18, Celal19, Celal20, Celal21, Celal22, Celal23, Celal24, Celal25, Celal26, Celal27, Celal28, Celal29, Celal30, Celal31, Celal32, Celal33, Celal34, Celal35, Celal36, Celal37, Celal38, Celal39, Celal40, Celal41, Celal42, Celal43]
        f = random.choice(CelalŞengörlist)
        embed = Embed(title="Celal Şengör derki", description=f)
        await ctx.response.send_message(embed=embed)
    if l == 7:
        Metehanlist = [Metehan1, Metehan2, Metehan3, Metehan4, Metehan5, Metehan6, Metehan7]
        f = random.choice(Metehanlist)
        embed = Embed(title="Metehan derki", description=f)
        await ctx.response.send_message(embed=embed)
    if l == 8:
        Einlist = [Ein1, Ein2,Ein3,Ein4,Ein5, Ein6,Ein7,Ein8,Ein9,Ein10,Ein11,Ein12,Ein13,Ein14,Ein15,Ein16,Ein17,Ein18]
        f = random.choice(Einlist)
        embed = Embed(title="Einstein derki", description=f)
        await ctx.response.send_message(embed=embed)

@Bot.command(name = "propaganda", description = "Random propaganda gönderir", guild = Object(id = uid))
async def propaganda(ctx: Interaction):
    propagandalist = [Propaganda1, Propaganda2, Propaganda3, Propaganda4, Propaganda5, Propaganda6, Propaganda7, Propaganda8, Propaganda9, Propaganda10, Propaganda11, Propaganda12, Propaganda13, Propaganda14, Propaganda15, Propaganda16, Propaganda17, Propaganda18, Propaganda19, Propaganda20, Propaganda21, Propaganda22, Propaganda23, Propaganda24, Propaganda25, Propaganda26, Propaganda27, Propaganda28, Propaganda29, Propaganda30, Propaganda31, Propaganda32, Propaganda33, Propaganda34, Propaganda35, Propaganda36, Propaganda37, Propaganda38, Propaganda39, Propaganda40, Propaganda41, Propaganda42, Propaganda43, Propaganda44, Propaganda45, Propaganda46, Propaganda47, Propaganda48, Propaganda49, Propaganda50, Propaganda51, Propaganda52, Propaganda53, Propaganda54, Propaganda55, Propaganda56, Propaganda57, Propaganda58, Propaganda59, Propaganda60, Propaganda61]
    await ctx.response.send_message(random.choice(propagandalist))


@Bot.command(name = "random", description = "Random öneride bulunur", guild = Object(id = uid))
async def r(ctx: Interaction, args: str):
    if "kitap" in args:
        page = requests.get("https://www.generatormix.com/random-book-generator")
        soup = BeautifulSoup(page.text, "lxml")
        a = soup.find("div", class_="col-7")
        b = a.text.replace("Get it on Amazon US", "")
        c = b.replace("Fiction", "Kurgu")
        d = c.replace("keywords", "Anahtar Kelimeler")
        e = d.replace("\n\n", "\n")
        f = e.replace("\nby ", "\nYazar: ")
        g = f.replace("Get it on Amazon DE", "")
        embed = Embed(title="Random Kitap Önerisi", description=f, color=0x990000)
        await ctx.response.send_message(embed=embed)
    if "film" in args:
        page = requests.get("https://www.generatormix.com/random-movie-generator")
        soup = BeautifulSoup(page.text, "lxml")
        a = soup.find("div", class_="thumbnail-col-3 tile-block-inner marg-top first")
        b = a.text.replace("Watch trailer", "")
        d = b.replace("Get it on Amazon US", "")
        embed = Embed(title="Random Film Önerisi", description=d, color=0x990000)
        await ctx.response.send_message(embed=embed)
    if "şarkı" in args:
        page = requests.get("https://www.generatormix.com/random-spotify-songs-generator")
        soup = BeautifulSoup(page.text, "lxml")
        a = soup.find("div", class_="thumbnail-col-3 tile-block-inner marg-top first")
        z = soup.find("a", class_="btn btn-default col-10 no-float btn-spotify marg-top")["href"]
        b = a.text.replace("No preview available.", "")
        c = b.replace(" Get track on Spotify", z)
        d = c.replace("Get it on Amazon US", "")
        embed = Embed(title="Random Şarkı Önerisi", description=str(d), color=0x990000)
        await ctx.response.send_message(embed=embed)
    if "oyun" in args:
        page = requests.get("https://www.generatormix.com/random-steam-games-generator")
        soup = BeautifulSoup(page.text, "lxml")
        a = soup.find("a", class_="btn btn-steam marg-bottom col-12")["href"]
        await ctx.response.send_message(a)
    if "anime" in args:
        query = '''
        query ($id: Int) { # Define which variables will be used in the query (id)
        Media (id: $id, type: ANIME) { # Insert our variables into the query arguments (id) (type: ANIME is hard-coded in the query)
            id
            title {
            romaji
            }
        }
        }
        '''
        l = random.randint(1, 9999)
        variables = {
            'id': l
        }
        url = 'https://graphql.anilist.co'
        response = requests.post(url, json={'query': query, 'variables': variables})
        a = json.loads(response.text)
        url = 'https://anilist.co/anime/' + str(l)
        u = a.get('data').get('Media').get('title').get('romaji')
        embed = Embed(title=u, description=url, color=0x990000)
        await ctx.response.send_message(embed=embed)
    if "manga" in args:
        l = random.randint(1, 20700)
        url = 'https://myanimelist.net/manga/' + str(l)
        embed = Embed(title="Random manga önerisi" ,description=url, color=0x990000)
        await ctx.response.send_message(embed=embed)


@Bot.command(name = "zar", description = "zar atar", guild = Object(id = uid))
async def zar(ctx: Interaction):
    z = random.randint(1, 6)
    embed = Embed(title="Zar atıldı!", description=z , color=0x990000)
    await ctx.response.send_message(embed=embed)


# HOI4 Tips

@Bot.command(name = "hoi4tip", description = "HOI4 önerisinde bulunur", guild = Object(id = uid))
async def hoi4tip(ctx: Interaction):
    Hoitiplist = [hoitip1, hoitip2, hoitip3, hoitip4, hoitip5, hoitip6, hoitip7, hoitip8, hoitip9, hoitip10, hoitip11, hoitip12, hoitip13, hoitip14, hoitip15, hoitip16, hoitip17, hoitip18, hoitip19, hoitip20, hoitip21, hoitip22, hoitip23, hoitip24, hoitip25, hoitip26, hoitip27, hoitip28, hoitip29, hoitip30, hoitip31, hoitip32, hoitip33, hoitip34, hoitip35, hoitip36, hoitip37, hoitip38, hoitip39, hoitip40, hoitip41, hoitip42, hoitip43, hoitip44, hoitip45]
    await ctx.response.send_message(random.choice(Hoitiplist))


# Dersler

@Bot.command(name = "ders", description = "manga-anime çeviri-edit dersi atar", guild = Object(id = uid))
async def ders(ctx: Interaction, ders: str):
    if "anime-çeviri" in ders:
        await ctx.response.send_message("https://i.imgur.com/DZBjYxg.jpg\nhttps://i.imgur.com/X5r544n.jpg")

# 4.1

@Bot.command(name = "cmm", description = "Yazdığınız şeyi change my mind miimi yapar", guild = Object(id = uid))
async def cmm(ctx: Interaction, meme: str):
    img = Image.open("change-my-mind.jpg")
    draw = ImageDraw.Draw(img)
    font = ImageFont.truetype("impact.ttf", 55, encoding="utf-8")
    metin = str(meme).replace("(", "")
    metin = metin.replace(")", "")
    metin = metin.replace("'", "")
    metin = metin.replace(",", "")
    metin = metin.replace("-", " ")
    y = 550
    for i, metin in enumerate(metin.split(' ')):
        draw.text((340, y),metin,(0,0,0),font=font)
        y = y + 60
    kdgh = "cmm/" + str(random.randint(0, 10000)) + ".jpg"
    img.save(kdgh)
    await ctx.response.send_message(' ', file=File(kdgh))
    
@Bot.command(name = "polska", description = "Sadece dene ve gör😏", guild = Object(id = uid))
async def polska(ctx: Interaction):
    if(ctx.author.voice):
        if vatoz != "cow": 
            dem = open("dancing-polish-cow-at4am.gif", 'rb')
            demo = dem.read()
            await client.change_presence(activity=Game(name="Tylko jedno w głowie mam Koksu pięc gram"))
            await client.user.edit(username="Polish Cow", avatar=demo)
        channel=ctx.ctx.author.voice.channel
        vc = await channel.connect()
        vc.play(FFmpegPCMAudio(executable="ffmpeg.exe", source="polish-cow-full-song.mp3"))
        await ctx.response.send_message("https://tenor.com/bqmYe.gif")
    else:   
        await ctx.response.send_message("Herhangi bir sesd sunucusunda değilsin!")

@Bot.command(name = "çık", description = "Vatozu bulunduğunuz kanaldan çıkarır", guild = Object(id = uid))
async def çık(ctx: Interaction):
    if(ctx.voice_client):
        await ctx.guild.voice_client.disconnect()
        await ctx.response.send_message("Ses sunucusundan çıktım")
    else:
        await ctx.response.send_message("Herhangi bir ses kanalımda değilim")

client.run(os.getenv('token'))

##=================================##
##=-Project:           BKControl -=##
##=-Author:         Adam Dvorsky -=##
##=-Date:             2020-08-17 -=##
##=================================##

class books:

    iBooks = [
        'Studijní předpoklady a základy logiky - 1.',
        'Studijní předpoklady a základy logiky - 2.',
        'Chcete se dostat na lékařskou fakultu? 1.',
        'Chcete se dostat na lékařskou fakultu? 2.',
        'Chcete se dostat na lékařskou fakultu? 3.',
        'Chcete se dostat na lékařskou fakultu? 4.',
        'Chcete se dostat na fakultu sociálních studií (věd)?',
        'Chcete se dostat na vysokou školu? Angličtina',
        'Chcete se dostat na VŠ? Němčina',
        'Chcete se dostat na ekonomickou fakultu 1.díl',
        'Chcete se dostat na právnickou fakultu? 1',
        'Chcete se dostat na právnickou fakultu? 2',
        'Jak se dostat na vysokou školu?',
        'Základy společenských věd - 1. díl',
    ]

# ----------- Dobrovsky -------------- #
    UrlDobr = [
        'https://www.knihydobrovsky.cz/kniha/studijni-predpoklady-a-zaklady-logiky-1-dil-13656514',
        'https://www.knihydobrovsky.cz/kniha/testy-obecnych-studijnich-predpokladu-a-zaklady-logiky-2-dil-22193474',
        'https://www.knihydobrovsky.cz/kniha/chcete-se-dostat-na-lekarskou-fakultu-chemie-1-dil-3-vydani-78643',
        'https://www.knihydobrovsky.cz/kniha/chcete-se-dostat-na-lekarskou-fakultu-biologie-2-dil-3-vydani-16777',
        'https://www.knihydobrovsky.cz/kniha/chcete-se-dostat-na-lekarskou-fakultu-fyzika-3-dil-3-vydani-88012',
        'https://www.knihydobrovsky.cz/kniha/chcete-se-dostat-na-lekarskou-fakultu-4-dil-biologie-fyzika-chemie-39686',
        'https://www.knihydobrovsky.cz/kniha/chcete-se-dostat-na-fakultu-socialnich-studii-ved-2-dil-3-vydani-88036',
        'https://www.knihydobrovsky.cz/kniha/chcete-se-dostat-na-vysokou-skolu-anglictina-2-vydani-25684',
        'https://www.knihydobrovsky.cz/kniha/chcete-se-dostat-na-vysokou-skolu-nemcina-79315',
        'https://www.knihydobrovsky.cz/kniha/chcete-se-dostat-na-ekonomickou-fakultu-1-dil-matematika-2-vydani-80897',
        'https://www.knihydobrovsky.cz/kniha/chcete-se-dostat-na-pravnickou-fakultu-1-dil-2-vydani-25432',
        'https://www.knihydobrovsky.cz/kniha/chcete-se-dostat-na-pravnickou-fakultu-2-dil-3-vydani-80731',
        'https://www.knihydobrovsky.cz/kniha/jak-se-dostat-na-vs-podrobny-pruvodce-prijimacim-rizenim-79316',
        'https://www.knihydobrovsky.cz/kniha/zaklady-spolecenskych-ved-i-dil-2-vydani-89733',

    ]

    PathDobr = {
        'BookStore' : 'Dobrovsky',
        'name'      : '//span[contains(@itemprop, "name")]',
        'url'       : '//*[@id="snippet-bookDetail-availabilityInfo"]/div/div[1]/ul/li[1]',
    }

    StockDobr = 'Skladem'

# ------------ Kosmas ---------------- #
    UrlKos = [
        'https://www.kosmas.cz/knihy/231633/studijni-predpoklady-a-zaklady-logiky-1.-dil/',
        'https://www.kosmas.cz/knihy/231623/studijni-predpoklady-a-zaklady-logiky-2.-dil/',
        'https://www.kosmas.cz/knihy/175416/chcete-se-dostat-na-lekarskou-fakultu-1.-dil-chemie/',
        'https://www.kosmas.cz/knihy/157334/chcete-se-dostat-na-lekarskou-fakultu-2.-dil-biologie/',
        'https://www.kosmas.cz/knihy/192198/chcete-se-dostat-na-lekarskou-fakultu-3.-dil-fyzika/',
        'https://www.kosmas.cz/knihy/158409/chcete-se-dostat-na-lekarskou-fakultu/',
        'https://www.kosmas.cz/knihy/277813/chcete-se-dostat-na-fakultu-socialnich-studii-ved-2.-dil/',
        'https://www.kosmas.cz/knihy/147435/chcete-se-dostat-na-vysokou-skolu-anglictina/',
        'https://www.kosmas.cz/knihy/137805/chcete-se-dostat-na-vs-nemcina/',
        'https://www.kosmas.cz/knihy/139500/chcete-se-dostat-na-ekonomickou-fakultu-1.dil-matematika/',
        'https://www.kosmas.cz/knihy/123964/chcete-se-dostat-na-pravnickou-fakultu-1/#pos=0',
        'https://www.kosmas.cz/knihy/178916/chcete-se-dostat-na-pravnickou-fakultu-2.-dil-vseobecny-prehled-a-zaklady-prava/',
        'https://www.kosmas.cz/knihy/137801/jak-se-dostat-na-vysokou-skolu/',
        'https://www.kosmas.cz/knihy/149448/zaklady-spolecenskych-ved-i.-dil/',
    ]

    PathKos = {
        'BookStore' : 'Kosmas',
        'name'      : '//h1[contains(@class, "product__title")]',
        'url'       : "//td[contains(@class, 'availability')]",
    }

    StockKos = 'Skladem'

    iRefsKos = [
        'studijni-predpoklady-a-zaklady-logiky-1.-dil',
        'studijni-predpoklady-a-zaklady-logiky-2.-dil',
        'chcete-se-dostat-na-lekarskou-fakultu-1.-dil',
        'chcete-se-dostat-na-lekarskou-fakultu-2.-dil',
        'chcete-se-dostat-na-lekarskou-fakultu-3.-dil',
        'chcete-se-dostat-na-lekarskou-fakultu',
        'chcete-se-dostat-na-fakultu-socialnich-studii-ved-2.-dil',
        'chcete-se-dostat-na-vysokou-skolu-anglictina',
        'chcete-se-dostat-na-vs-nemcina',
        'chcete-se-dostat-na-ekonomickou-fakultu-1.dil-matematika',
        'chcete-se-dostat-na-pravnickou-fakultu-1',
        'chcete-se-dostat-na-pravnickou-fakultu-2',
        'jak-se-dostat-na-vysokou-skolu',
    ]

# ------------ Luxor ----------------- #
    UrlLux = [
        'https://www.luxor.cz/product/studijni-predpoklady-a-zaklady-logiky-1-dil-zbo000198618',
        'https://www.luxor.cz/product/studijni-predpoklady-a-zaklady-logiky-2-dil-zbo000198619',
        'https://www.luxor.cz/product/chcete-se-dostat-na-lekarskou-fakultu-zbo000198614',
        'https://www.luxor.cz/product/chcete-se-dostat-na-lekarskou-fakultu-2-dil-zbo000198608',
        'https://www.luxor.cz/product/chcete-se-dostat-na-lekarskou-fakultu-3-dil-fyzika-zbo000198615',
        'https://www.luxor.cz/product/chcete-se-dostat-na-lekarskou-fakultu-4-dil-zbo000198607',
        'https://www.luxor.cz/product/chcete-se-dostat-na-fakultu-socialnich-studii-ved-zbo000198612',
        'https://www.luxor.cz/product/chcete-se-dostat-na-vysokou-skolu-anglictina-zbo000198603',
        'https://www.luxor.cz/product/chcete-se-dostat-na-vysokou-skolu-nemcina-zbo000198596',
        'https://www.luxor.cz/product/chcete-se-dostat-na-ekon-fak-1-dil-matematika-zbo000198598',
        'https://www.luxor.cz/product/chcete-se-dostat-na-pravnickou-fakultu-zbo000198604',
        'https://www.luxor.cz/product/chcete-se-dostat-na-pravnickou-fakultu-2-dil-vseobecny-prehled-a-zaklady-pra-zbo000198611',
        'https://www.luxor.cz/product/jak-se-dostat-na-vysokou-skolu-zbo000198595',
        'https://www.luxor.cz/product/zaklady-spolecenskych-ved-i-zbo000198616',
    ]

    PathLux = {
        'BookStore' : 'Luxor',
        'name'      : '//div[contains(@class, "ant-col ant-col-xs-24 ant-col-md-12")]',
        'url'       : '//div[contains(@class, "f1ubm3q7")]',
    }

    StockLux = 'SKLADEM'

# ----------- Martinus --------------- #
    UrlMar = [
        'https://www.martinus.cz/?uItem=269503',
        'https://www.martinus.cz/?uItem=272399',
        'https://www.martinus.cz/?uItem=126108',
        'https://www.martinus.cz/?uItem=107528',
        'https://www.martinus.cz/?uItem=347825',
        'https://www.martinus.cz/?uItem=103364',
        'https://www.martinus.cz/?uItem=397501',
        'https://www.martinus.cz/?uItem=67118',
        'https://www.martinus.cz/?uItem=416793',
        'https://www.martinus.cz/?uItem=46125',
        'https://www.martinus.cz/?uItem=63128',
        'https://www.martinus.cz/?uItem=46128',
        'https://www.martinus.cz/?uItem=128682',
        'https://www.martinus.cz/?uItem=422595',
    ]

    PathMar = {
        'BookStore' : 'Martinus',
        'name'      : '//h1[contains(@class, "product-detail__title mb-small")]',
        'url'       : '//*[@id="web"]/article/div[2]', 
    }

    StockMar = 'Na skladě'

    # //*[@id="web"]/article/div[2]
    # //*[@id="web"]/article/div[2]
    # //*[@id="web"]/article/div[2]

# ---------- Megaknihy --------------- #
    iBooksMK = {
        'Studijní předpoklady a základy logiky - 1.'            : 'https://www.megaknihy.cz/ostatni/267298-studijni-predpoklady-a-zaklady-logiky-1-dil.html?search_pos=1',
        'Studijní předpoklady a základy logiky - 2.'            : 'https://www.megaknihy.cz/maturita-prijimacky/268969-testy-obecnych-studijnich-predpokladu-a-zaklady-logiky-2-dil.html?block=edition&position=2',
        'Chcete se dostat na lékařskou fakultu? 1.'             : 'https://www.megaknihy.cz/cizi-jazyky/140214-chcete-se-dostat-na-lekarskou-fakultu-chemie-1-dil-3-vydani.html?search_pos=1',
        'Chcete se dostat na lékařskou fakultu? 2.'             : 'https://www.megaknihy.cz/cizi-jazyky/95132-chcete-se-dostat-na-lekarskou-fakultu-2-dil.html?search_pos=1',
        'Chcete se dostat na lékařskou fakultu? 3.'             : 'https://www.megaknihy.cz/cizi-jazyky/149616-chcete-se-dostat-na-lekarskou-fakultu-fyzika-3-dil-3-vydani.html?search_pos=1',
        'Chcete se dostat na lékařskou fakultu? 4.'             : 'https://www.megaknihy.cz/stredni-skola/95133-chcete-se-dostat-na-lekarskou-fakultu-4-dil-biologie-fyzika-chemie.html?search_pos=1',
        'Chcete se dostat na fakultu sociálních studií (věd)?'  : 'https://www.megaknihy.cz/cizi-jazyky/145060-chcete-se-dostat-na-fakultu-socialnich-studii-ved.html?search_pos=1',
        'Chcete se dostat na vysokou školu? Angličtina'         : 'https://www.megaknihy.cz/cizi-jazyky/57164-chcete-se-dostat-na-vysokou-skolu-anglictina.html?search_pos=1',
        'Chcete se dostat na VŠ? Němčina'                       : 'https://www.megaknihy.cz/cizi-jazyky/42750-chcete-se-dostat-na-vysokou-skolu-nemcina.html?search_pos=2',
        'Chcete se dostat na ekonomickou fakultu 1.díl'         : 'https://www.megaknihy.cz/cizi-jazyky/50493-chcete-se-dostat-na-ekonomickou-fakultu-1-dil.html?search_pos=1',
        'Chcete se dostat na právnickou fakultu? 1'             : 'https://www.megaknihy.cz/cizi-jazyky/57167-chcete-se-dostat-na-pravnickou-fakultu.html?search_pos=1',
        'Chcete se dostat na právnickou fakultu? 2'             : 'https://www.megaknihy.cz/cizi-jazyky/129347-chcete-se-dostat-na-pravnickou-fakultu-2-dil.html?search_pos=1',
        'Jak se dostat na vysokou školu?'                       : 'https://www.megaknihy.cz/cizi-jazyky/46834-jak-se-dostat-na-vysokou-skolu.html?search_pos=1',
        'Základy společenských věd - 1. díl'                    : 'https://www.megaknihy.cz/cizi-jazyky/150910-zaklady-spolecenskych-ved-i-dil-2-vydani.html?search_pos=1'
    }

    UrlMK = [
        'https://www.megaknihy.cz/ostatni/267298-studijni-predpoklady-a-zaklady-logiky-1-dil.html',
        'https://www.megaknihy.cz/maturita-prijimacky/268969-testy-obecnych-studijnich-predpokladu-a-zaklady-logiky-2-dil.html?block=edition&position=2',
        'https://www.megaknihy.cz/cizi-jazyky/140214-chcete-se-dostat-na-lekarskou-fakultu-chemie-1-dil-3-vydani.html',
        'https://www.megaknihy.cz/cizi-jazyky/95132-chcete-se-dostat-na-lekarskou-fakultu-2-dil.html?block=edition&position=1',
        'https://www.megaknihy.cz/cizi-jazyky/149616-chcete-se-dostat-na-lekarskou-fakultu-fyzika-3-dil-3-vydani.html?block=edition&position=4',
        'https://www.megaknihy.cz/stredni-skola/95133-chcete-se-dostat-na-lekarskou-fakultu-4-dil-biologie-fyzika-chemie.html?block=edition&position=2',
        'https://www.megaknihy.cz/cizi-jazyky/145060-chcete-se-dostat-na-fakultu-socialnich-studii-ved.html?search_pos=1',
        'https://www.megaknihy.cz/cizi-jazyky/57164-chcete-se-dostat-na-vysokou-skolu-anglictina.html?block=related&position=11',
        'https://www.megaknihy.cz/cizi-jazyky/42750-chcete-se-dostat-na-vysokou-skolu-nemcina.html',
        'https://www.megaknihy.cz/cizi-jazyky/50493-chcete-se-dostat-na-ekonomickou-fakultu-1-dil.html',
        'https://www.megaknihy.cz/cizi-jazyky/57167-chcete-se-dostat-na-pravnickou-fakultu.html',
        'https://www.megaknihy.cz/cizi-jazyky/129347-chcete-se-dostat-na-pravnickou-fakultu-2-dil.html?block=edition&position=2',
        'https://www.megaknihy.cz/cizi-jazyky/46834-jak-se-dostat-na-vysokou-skolu.html',
        'https://www.megaknihy.cz/cizi-jazyky/150910-zaklady-spolecenskych-ved-i-dil-2-vydani.html',
    ]

    PathMK = {
        'BookStore' : 'Megaknihy',
        'name'      : '//span[contains(@itemprop, "name")]',
        'url'       : '//span[contains(@class, "avail_now_text")]',
    }

    StockMK = 'máme skladem'

# ---------- ABZKnihy ---------------- #
    iBooksABZ = {
        'Studijní předpoklady a základy logiky - 1.'            : 'https://knihy.abz.cz/prodej/studijni-predpoklady-a-zaklady-logiky-1-dil-teorie-a-priklady',
        'Studijní předpoklady a základy logiky - 2.'            : 'https://knihy.abz.cz/prodej/testy-obecnych-studijnich-predpokladu-a-zaklady-logiky-2-dil',
        'Chcete se dostat na lékařskou fakultu? 1.'             : 'https://knihy.abz.cz/prodej/chcete-se-dostat-na-lekarskou-fakultu-1-dil-chemie-220-otazek-a-z-prijimacich-zkousek-s-resenim',
        'Chcete se dostat na lékařskou fakultu? 2.'             : 'https://knihy.abz.cz/prodej/chcete-se-dostat-na-lekarskou-fakultu-biologie-2-dil',
        'Chcete se dostat na lékařskou fakultu? 3.'             : 'https://knihy.abz.cz/prodej/chcete-se-dostat-na-lekarskou-fakultu-3-dil',
        'Chcete se dostat na lékařskou fakultu? 4.'             : 'https://knihy.abz.cz/prodej/chcete-se-dostat-na-lekarskou-fakultu-4-dil-cvicebnice-testovych-otazek',
        'Chcete se dostat na fakultu sociálních studií (věd)?'  : 'https://knihy.abz.cz/prodej/chcete-se-dostat-na-fakultu-socialnich-studii-ved-psychologie-a-sociologie-filozofie-a-politicka-filozofie-politologie',
        'Chcete se dostat na vysokou školu? Angličtina'         : 'https://knihy.abz.cz/prodej/chcete-se-dostat-na-vysokou-skolu-anglictina-500-testovych-otazek-z-prijimacich-zkousek-s-resenim',
        'Chcete se dostat na VŠ? Němčina'                       : 'https://knihy.abz.cz/prodej/chcete-se-dostat-na-vysokou-skolu-nemcina',
        'Chcete se dostat na ekonomickou fakultu 1.díl'         : 'https://knihy.abz.cz/prodej/chcete-se-dostat-na-ekonomickou-fakultu-1-dil',
        'Chcete se dostat na právnickou fakultu? 1'             : 'https://knihy.abz.cz/prodej/chcete-se-dostat-na-pravnickou-fakultu-1-dil-2-vydani',
        'Chcete se dostat na právnickou fakultu? 2'             : 'https://knihy.abz.cz/prodej/chcete-se-dostat-na-pravnickou-fakultu-2-dil-1',
        'Jak se dostat na vysokou školu?'                       : 'https://knihy.abz.cz/prodej/jak-se-dostat-na-vysokou-skolu',
        'Základy společenských věd - 1. díl'                    : 'https://knihy.abz.cz/prodej/zaklady-spolecenskych-ved-i-dil-1',
    }

    UrlABZ = [
        'https://knihy.abz.cz/prodej/studijni-predpoklady-a-zaklady-logiky-1-dil-teorie-a-priklady',
        'https://knihy.abz.cz/prodej/testy-obecnych-studijnich-predpokladu-a-zaklady-logiky-2-dil',
        'https://knihy.abz.cz/prodej/chcete-se-dostat-na-lekarskou-fakultu-1-dil-chemie-220-otazek-a-z-prijimacich-zkousek-s-resenim',
        'https://knihy.abz.cz/prodej/chcete-se-dostat-na-lekarskou-fakultu-biologie-2-dil',
        'https://knihy.abz.cz/prodej/chcete-se-dostat-na-lekarskou-fakultu-3-dil',
        'https://knihy.abz.cz/prodej/chcete-se-dostat-na-lekarskou-fakultu-4-dil-cvicebnice-testovych-otazek',
        'https://knihy.abz.cz/prodej/chcete-se-dostat-na-fakultu-socialnich-studii-ved-psychologie-a-sociologie-filozofie-a-politicka-filozofie-politologie',
        'https://knihy.abz.cz/prodej/chcete-se-dostat-na-vysokou-skolu-anglictina-500-testovych-otazek-z-prijimacich-zkousek-s-resenim',
        'https://knihy.abz.cz/prodej/chcete-se-dostat-na-vysokou-skolu-nemcina',
        'https://knihy.abz.cz/prodej/chcete-se-dostat-na-ekonomickou-fakultu-1-dil',
        'https://knihy.abz.cz/prodej/chcete-se-dostat-na-pravnickou-fakultu-1-dil-2-vydani',
        'https://knihy.abz.cz/prodej/chcete-se-dostat-na-pravnickou-fakultu-2-dil-1',
        'https://knihy.abz.cz/prodej/jak-se-dostat-na-vysokou-skolu',
        'https://knihy.abz.cz/prodej/zaklady-spolecenskych-ved-i-dil-1',
    ]

    PathABZ = {
        'BookStore' : 'ABZ Knihy',
        'name'      : '//span[contains(@itemprop, "name")]',
        # 'name'  : '//*[@id="content_part"]/div[2]/article/div/h2/span[1]',
        'url'       : '//span[contains(@class, "dostupnost")]',
    }

    StockABZ = 'skladem'

# --------- Knihcentrum -------------- #
    UrlKC = [
        'https://www.knihcentrum.cz/studijni-predpoklady-a-zaklady-logiky-1dil',
        'https://www.knihcentrum.cz/studijni-predpoklady-a-zaklady-logiky-2-dil',
        'https://www.knihcentrum.cz/chcete-se-dostat-na-lekarskou-fakultu-1',
        'https://www.knihcentrum.cz/chcete-se-dostat-na-lekarskou-fakultu-2dil-2',
        'https://www.knihcentrum.cz/chcete-se-dostat-na-lekarskou-fakultu-3dil-2',
        'https://www.knihcentrum.cz/chcete-se-dostat-na-lekarskou-fakultu-3dil-2',
        'https://www.knihcentrum.cz/chcete-se-dostat-na-fakultu-socialnich-studii-ved-2-dil',
        'https://www.knihcentrum.cz/chcete-se-dostat-na-vysokou-skolu-anglictina-1',
        'https://www.knihcentrum.cz/chcete-se-dostat-na-vysokou-skolu-nemcina',
        'https://www.knihcentrum.cz/chcete-se-dostat-na-ekonomickou-fakultu-1dil',
        'https://www.knihcentrum.cz/chcete-se-dostat-na-pravnickou-fakultu-3',
        'https://www.knihcentrum.cz/chcete-se-dostat-na-pravnickou-fakultu-2-dil',
        'https://www.knihcentrum.cz/chcete-se-dostat-na-vysokou-skolu-nemcina',
        'https://www.knihcentrum.cz/zaklady-spolecenskych-ved-i-1',
    ]

    PathKC = {
        'BookStore' : 'Knihcentrum',
        'name'      : '//h1[contains(@itemprop, "name")]',
        'url'       : '//span[contains(@class, "stock-name")]',
    }

    StockKC = 'IHNED odesíláme'

    iBooksKC = {
        'Studijní předpoklady a základy logiky - 1.'                : 'https://www.knihcentrum.cz/studijni-predpoklady-a-zaklady-logiky-1dil',
        'Studijní předpoklady a základy logiky - 2.'                : 'https://www.knihcentrum.cz/studijni-predpoklady-a-zaklady-logiky-2-dil',
        'Chcete se dostat na lékařskou fakultu? 1.'                 : 'https://www.knihcentrum.cz/chcete-se-dostat-na-lekarskou-fakultu-1',
        'Chcete se dostat na lékařskou fakultu? 2.'                 : 'https://www.knihcentrum.cz/chcete-se-dostat-na-lekarskou-fakultu-2dil-2',
        'Chcete se dostat na lékařskou fakultu? 3.'                 : 'https://www.knihcentrum.cz/chcete-se-dostat-na-lekarskou-fakultu-3dil-2',
        'Chcete se dostat na lékařskou fakultu? 4.'                 : 'https://www.knihcentrum.cz/chcete-se-dostat-na-lekarskou-fakultu-3dil-2',
        'Chcete se dostat na fakultu sociálních studií (věd)?'      : 'https://www.knihcentrum.cz/chcete-se-dostat-na-fakultu-socialnich-studii-ved-2-dil',
        'Chcete se dostat na vysokou školu? Angličtina'             : 'https://www.knihcentrum.cz/chcete-se-dostat-na-vysokou-skolu-anglictina-1',
        'Chcete se dostat na VŠ? Němčina'                           : 'https://www.knihcentrum.cz/chcete-se-dostat-na-vysokou-skolu-nemcina',
        'Chcete se dostat na ekonomickou fakultu 1.díl'             : 'https://www.knihcentrum.cz/chcete-se-dostat-na-ekonomickou-fakultu-1dil',
        'Chcete se dostat na právnickou fakultu? 1'                 : 'https://www.knihcentrum.cz/chcete-se-dostat-na-pravnickou-fakultu-3',
        'Chcete se dostat na právnickou fakultu? 2'                 : 'https://www.knihcentrum.cz/chcete-se-dostat-na-pravnickou-fakultu-2-dil',
        'Jak se dostat na vysokou školu?'                           : 'https://www.knihcentrum.cz/chcete-se-dostat-na-vysokou-skolu-nemcina',
        'Základy společenských věd - 1. díl'                        : 'https://www.knihcentrum.cz/zaklady-spolecenskych-ved-i-1',
    }

# ------------ Knihy ----------------- #
    UrlKnihy = [
        'https://www.knihy.cz/studijni-predpoklady-a-zaklady-logiky-1-dil/',
        'https://www.knihy.cz/studijni-predpoklady-a-zaklady-logiky-2-dil/',
        # '', # lekarska 1
        # '', # lekarska 2
        'https://www.knihy.cz/chcete-se-dostat-na-lekarskou-fakultu-3-dil/',
        'https://www.knihy.cz/chcete-se-dostat-na-lekarskou-fakultu-4-dil/',
        'https://www.knihy.cz/chcete-se-dostat-na-fakultu-socialnich-studii-ved/',
        # '', # anglictina
        'https://www.knihy.cz/chcete-se-dostat-na-vysokou-skolu-nemcina/',
        'https://www.knihy.cz/chcete-se-dostat-na-ekonomickou-fakultu-1-dil/',
        'https://www.knihy.cz/chcete-se-dostat-na-pravnickou-fakultu/',
        # '', # pravnicka 2
        'https://www.knihy.cz/jak-se-dostat-na-vysokou-skolu/',
        'https://www.knihy.cz/zaklady-spolecenskych-ved-i/',
    ]

    PathKnihy = {
        'BookStore' : 'Knihy.cz',
        'name'      : '//h1[contains(@class, "box-detail__info__title")]',
        'url'       : '//div[contains(@class, "box-detail__info__availability box-detail__info__availability--code-inStock")]'
    }

    StockKnihy = 'Skladem 5+ ks'

# ----------- BookTook --------------- #
    UrlBT = [
        'https://www.booktook.cz/p/testy-obecnych-studijnich-predpokladu-a-zaklady-logiky-1-dil-9788086572802/', # 11. editon
        'https://www.booktook.cz/p/testy-obecnych-studijnich-predpokladu-a-zaklady-logiky-2-dil/',
        'https://www.booktook.cz/p/chcete-se-dostat-na-lekarskou-fakultu-chemie-1-dil-3-vydani-220-otazek-z-prijimacich-zkousek-s-resenim/',
        'https://www.booktook.cz/p/chcete-se-dostat-na-lekarskou-fakultu-biologie-2-dil/',
        'https://www.booktook.cz/p/chcete-se-dostat-na-lekarskou-fakultu-fyzika-3-dil-9788086572741/',
        'https://www.booktook.cz/p/chcete-se-dostat-na-lekarskou-fakultu-4-dil-biologie-fyzika-chemie-cvicebnice-testovych-otazek/',
        'https://www.booktook.cz/p/chcete-se-dostat-na-fakultu-socialnich-studii-ved-2-dil-3-vydani-psychologie-a-sociologie-filozofie-a-politicka-filozofie-politologie/',
        # '', # anglictina
        # '', # nemcina
        # '', # ekonomika
        # '', # prava 1
        'https://www.booktook.cz/p/chcete-se-dostat-na-pravnickou-fakultu-2-dil-3-vydani/',
        # '', # vs
        'https://www.booktook.cz/p/zaklady-spolecenskych-ved-i-dil-priprava-pro-prijimaci-zkousky-na-vysoke-skoly/',
    ]

    PathBT = {
        'BookStore' : 'BookTook',
        'name'      : '//*[@id="det-main"]/div[1]/h1/span',
        'url'       : '//*[@id="det-buy"]/div/fieldset' 
    }

    StockBT = 'Skladem'

# ------------- sevt ----------------- #
    UrlSevt = [
        'https://www.sevt.cz/produkt/studijni-predpoklady-a-zaklady-logiky-1-dil-724l15349065/',
        # '', # 'zaklady logiky 2',
        'https://www.sevt.cz/produkt/chcete-se-dostat-na-lekarskou-fakultu-1-dil-chemie-3-vydani-n0055705/',
        'https://www.sevt.cz/produkt/chcete-se-dostat-na-lekarskou-fakultu-2-dil-biologie-3-vydani-n0055005/',
        # '', # 'lekarska 3.',
        'https://www.sevt.cz/produkt/chcete-se-dostat-na-lekarskou-fakultu-4-dil-fyzika-n0063705/',
        'https://www.sevt.cz/produkt/chcete-se-dostat-na-fakultu-socialnich-studii-2-dil-3-vydani-n0055605/.',
        # '', # 'anglictina',
        'https://www.sevt.cz/produkt/chcete-se-dostat-na-vs-nemcina-n0055805/',
        # '', # 'ekonomicka',
        'https://www.sevt.cz/produkt/chcete-se-dostat-na-pravnickou-fakultu-1-dil-3-vydani-n0054805/',
        # '', # 'prava 2.',
        # '', # 'jak se dostat na vs',
        # '', # 'zaklady spol ved 1.',
    ]

    PathSevt = {
        'BookStore' : 'SEVT',
        'name'      : '//h1[contains(@itemprop, "name")]',
        'url'       : '//span[contains(@class, "stock")]'
    }

    StockSevt = 'skladem'

# ---------- DumKnihy ---------------- #
    UrlDK = [
        'https://www.dumknihy.cz/studijni-predpoklady-a-zaklady-logiky-1-dil',
        'https://www.dumknihy.cz/studijni-predpoklady-a-zaklady-logiky-2-dil',
        'https://www.dumknihy.cz/svetske-kanony-duchovni-kanony',
        'https://www.dumknihy.cz/chcete-se-dostat-na-lekarskou-fakultu-109980',
        'https://www.dumknihy.cz/chcete-se-dostat-na-lekarskou-fakultu-fyzika-3-dil',
        'https://www.dumknihy.cz/chcete-se-dostat-na-lekarskou-fakultu-113058',
        'https://www.dumknihy.cz/chcete-se-dostat-na-fakultu-socialnich-studii-ved-2-dil-136012',
        'https://www.dumknihy.cz/chcete-se-dostat-na-vysokou-skolu',
        'https://www.dumknihy.cz/chcete-se-dostat-na-vysokou-skolu-74409',
        'https://www.dumknihy.cz/chcete-se-dostat-na-ekonomickou-fakultu-78506',
        'https://www.dumknihy.cz/chcete-se-dostat-na-pravnickou-fakultu-1-dil-90124',
        'https://www.dumknihy.cz/chcete-se-dostat-na-pravnickou-fakultu-2-dil-140074',
        # '', # jak se dostat na vs
        'https://www.dumknihy.cz/zaklady-spolecenskych-ved-i-dil-137766',
    ]

    PathDK = {
        'BookStore' : 'DumKnihy',
        'name'      : '//*[@id="breadcrumbs"]/p',
        'url'       : '//p[contains(@class, "availability yes")]'
    }

    StockDK = 'je skladem'

# ----------- Ladvi ------------------ #
    UrlLadvi = [
        # studijni predpoklady 1
        # studijni predpoklady 2
        'https://www.knihkupectvi-ladvi.cz/chcete-se-dostat-na-lekarskou-fakultu-p50740/',
        'https://www.knihkupectvi-ladvi.cz/chcete-se-dostat-na-lekarskou-fakultu-biologie-2-dil-3-vydani-p33520/',
        'https://www.knihkupectvi-ladvi.cz/chcete-se-dostat-na-lekarskou-fakultu-fyzika-3-dil-3-vydani-p61020/',
        'https://www.knihkupectvi-ladvi.cz/chcete-se-dostat-na-lekarskou-fakultu-4-dil-p45384/',
        'https://www.knihkupectvi-ladvi.cz/chcete-se-dostat-na-fakultu-socialnich-studii-ved-p43584/',
        'https://www.knihkupectvi-ladvi.cz/chcete-se-dostat-na-vysokou-skolu-p13118/',
        'https://www.knihkupectvi-ladvi.cz/chcete-se-dostat-na-vysokou-skolu-nemcina-p6170/',
        'https://www.knihkupectvi-ladvi.cz/chcete-se-dostat-na-ekonomickou-fakultu-1-dil-p5925/',
        'https://www.knihkupectvi-ladvi.cz/chcete-se-dostat-na-pravnickou-fakultu-1-dil-3-vydani-p13819/',
        'https://www.knihkupectvi-ladvi.cz/chcete-se-dostat-na-pravnickou-fakultu-3-dil-p45385/',
        'https://www.knihkupectvi-ladvi.cz/jak-se-dostat-na-vysokou-skolu-p5924/',
        'https://www.knihkupectvi-ladvi.cz/zaklady-spolecenskych-ved-i-dil-2-vydani-p63667/',
    ]

    PathLadvi = {
        'BookStore' : 'Ladvi',
        'name'      : '//h1[contains(@class, "HeadingView v2a v2 Heading")]',
        'url'       : '//span[contains(@class, "label")]'
    }

    StockLadvi = 'Skladem'

# ---------- Ucebnice.cz -------------- #
    UrlUce = [
        'https://www.ucebnice.cz/ostatni/267298-studijni-predpoklady-a-zaklady-logiky-1-dil.html',
        'https://www.ucebnice.cz/maturita-prijimacky/268969-testy-obecnych-studijnich-predpokladu-a-zaklady-logiky-2-dil.html',
        'https://www.ucebnice.cz/cizi-jazyky/140214-chcete-se-dostat-na-lekarskou-fakultu-chemie-1-dil-3-vydani.html',
        'https://www.ucebnice.cz/cizi-jazyky/95132-chcete-se-dostat-na-lekarskou-fakultu-2-dil.html',
        'https://www.ucebnice.cz/cizi-jazyky/149616-chcete-se-dostat-na-lekarskou-fakultu-fyzika-3-dil-3-vydani.html',
        'https://www.ucebnice.cz/stredni-skola/95133-chcete-se-dostat-na-lekarskou-fakultu-4-dil.html',
        'https://www.ucebnice.cz/cizi-jazyky/145060-chcete-se-dostat-na-fakultu-socialnich-studii-ved.html',
        'https://www.ucebnice.cz/cizi-jazyky/57164-chcete-se-dostat-na-vysokou-skolu-anglictina.html',
        'https://www.ucebnice.cz/cizi-jazyky/42750-chcete-se-dostat-na-vysokou-skolu-nemcina.html',
        'https://www.ucebnice.cz/cizi-jazyky/50493-chcete-se-dostat-na-ekonomickou-fakultu-1-dil.html',
        'https://www.ucebnice.cz/cizi-jazyky/57167-chcete-se-dostat-na-pravnickou-fakultu.html',
        'https://www.ucebnice.cz/cizi-jazyky/129347-chcete-se-dostat-na-pravnickou-fakultu-2-dil.html',
        'https://www.ucebnice.cz/cizi-jazyky/46834-jak-se-dostat-na-vysokou-skolu.html',
        'https://www.ucebnice.cz/cizi-jazyky/46834-jak-se-dostat-na-vysokou-skolu.html',
    ]


    PathUce = {
        'BookStore' : 'Ucebnice.cz',
        'name'      : '//span[contains(@itemprop, "name")]',
        'url'       : '//*[@id="pb-right-column"]/div[1]/div/div/div/strong',
        # 'url'   : '//link[contains(@itemprop, "availability")]',
    }

    StockUce = 'skladem'

# ---------- Beletrie -------------- #
    UrlBel = [
        'https://www.beletrie.eu/testy-obecnych-studijnich-predpokladu-a-zaklady-logiky-1-dil-p299139/',
        'https://www.beletrie.eu/testy-obecnych-studijnich-predpokladu-a-zaklady-logiky-2-dil-p303528/',
        'https://www.beletrie.eu/chcete-se-dostat-na-lekarskou-fakultu-p50740/',
        'https://www.beletrie.eu/chcete-se-dostat-na-lekarskou-fakultu-biologie-2-dil-3-vydani-p33520/',
        'https://www.beletrie.eu/chcete-se-dostat-na-lekarskou-fakultu-fyzika-3-dil-3-vydani-p61020/',
        'https://www.beletrie.eu/chcete-se-dostat-na-lekarskou-fakultu-4-dil-p45384/',
        'https://www.beletrie.eu/chcete-se-dostat-na-fakultu-socialnich-studii-ved-p43584/',
        'https://www.beletrie.eu/chcete-se-dostat-na-vysokou-skolu-anglictina-2-vydani-p15368/',
        'https://www.beletrie.eu/chcete-se-dostat-na-vysokou-skolu-nemcina-p6170/',
        'https://www.beletrie.eu/chcete-se-dostat-na-ekonomickou-fakultu-1-dil-p5925/',
        'https://www.beletrie.eu/chcete-se-dostat-na-pravnickou-fakultu-1-dil-3-vydani-p13819/',
        'https://www.beletrie.eu/chcete-se-dostat-na-pravnickou-fakultu-3-dil-p45385/',
        'https://www.beletrie.eu/jak-se-dostat-na-vysokou-skolu-p5924/',
        'https://www.beletrie.eu/zaklady-spolecenskych-ved-i-dil-2-vydani-p63667/',
    ]


    PathBel = {
        'BookStore' : 'Beletrie',
        'name'      : '//h1[contains(@class, "HeadingView v2a v2 Heading")]',
        'url'       : '//div[contains(@id, "w398516")]',
    }

    StockBel = 'skladem'

# ----------- Libristo ------------- #
    UrlLib = [
        'https://www.libristo.cz/cs/kniha/studijni-predpoklady-a-zaklady-logiky-1-dil_15872390',
        'https://www.libristo.cz/cs/kniha/testy-obecnych-studijnich-predpokladu-a-zaklady-logiky-2-dil_16244991',
        'https://www.libristo.cz/cs/kniha/chcete-se-dostat-na-lekarskou-fakultu_00127067',
        'https://www.libristo.cz/cs/kniha/chcete-se-dostat-na-lekarskou-fakultu-2-dil_00115215',
        'https://www.libristo.cz/cs/kniha/chcete-se-dostat-na-lekarskou-fakultu-3-dil_00136790',
        'https://www.libristo.cz/cs/kniha/chcete-se-dostat-na-lekarskou-fakultu-4-dil_00115216',
        'https://www.libristo.cz/cs/kniha/chcete-se-dostat-na-fakultu-socialnich-studii-ved_00123684',
        'https://www.libristo.cz/cs/kniha/chcete-se-dostat-na-vysokou-skolu-anglictina_00092199',
        'https://www.libristo.cz/cs/kniha/chcete-se-dostat-na-vysokou-skolu-nemcina_00074426',
        'https://www.libristo.cz/cs/kniha/chcete-se-dostat-na-ekonomickou-fakultu-1-dil_00083949',
        'https://www.libristo.cz/cs/kniha/chcete-se-dostat-na-pravnickou-fakultu_00092203',
        'https://www.libristo.cz/cs/kniha/chcete-se-dostat-na-pravnickou-fakultu-2-dil_00118335',
        'https://www.libristo.cz/czs/kniha/jak-se-dostat-na-vysokou-skolu_00079586',
        'https://www.libristo.cz/cs/kniha/zaklady-spolecenskych-ved-i_00139890',
    ]

    PathLib = {
        'BookStore' : 'Libristo',
        'name'      : '//*[@id="app"]/section[1]/div/div[3]/div[1]/h1',
        'ulr'       : '//div[contains(@class, "c-stock-avalibility")]',
    }

    StockLib = 'do 48 hodin'

# ----------- Knizniarcha ------------ #
    UrlArch = [
        # studijni predpoklady 1
        'https://www.knizniarcha.cz/studijni-predpoklady-a-zaklady-logiky-2.-dil',
        # '', # lekarska 1
        'https://www.knizniarcha.cz/chcete-se-dostat-na-lekarskou-fakultu--2.-dil-biologie',
        'https://www.knizniarcha.cz/studijni-predpoklady-a-zaklady-logiky-2.-dil',
        'https://www.knizniarcha.cz/chcete-se-dostat-na-lekarskou-fakultu--4.dil',
        'https://www.knizniarcha.cz/chcete-se-dostat-na-fakultu-socialnich-studii--ved--',
        # '', # anglictina
        # '', # nemcina
        'https://www.knizniarcha.cz/chcete-se-dostat-na-ekonomickou-fakultu-1.dil',
        'https://www.knizniarcha.cz/kalabis--radim---chcete-se-dostat-na-pravnickou-fakultu--1',
        'https://www.knizniarcha.cz/kotlan--igor---chcete-se-dostat-na-pravnickou-fakultu--2.-dil---vseobecny-prehled-a-zaklady-prava',
        'https://www.knizniarcha.cz/jak-se-dostat-na-vysokou-skolu-',
        'https://www.knizniarcha.cz/zaklady-spolecenskych-ved-i.',
    ]

    PathArch = {
        'BookStore' : 'Knizniarcha',
        'name'      : '//*[@id="product_detail"]/div/div[1]/div[2]/div[2]/h1',
        'url'       : '//div[contains(@class, "availability")]',
    }

    StockArch = 'Skladem'

# ----------- Books.cz -------------- #
    UrlBooks = [
        'https://www.books.cz/studijni-predpoklady-a-zaklady-logiky-1-dil-2/',
        'https://www.books.cz/studijni-predpoklady-a-zaklady-logiky-2-dil/',
        # '', # lekarska 1
        # '', # lekarska 2
        'https://www.books.cz/chcete-se-dostat-na-lekarskou-fakultu-3-dil-2/',
        'https://www.books.cz/chcete-se-dostat-na-lekarskou-fakultu-4-dil-3/',
        'https://www.books.cz/chcete-se-dostat-na-fakultu-socialnich-studii-ved-2/',
        'https://www.books.cz/chcete-se-dostat-na-vysokou-skolu-anglictina-2/',
        'https://www.books.cz/chcete-se-dostat-na-vysokou-skolu-nemcina-2/',
        'https://www.books.cz/chcete-se-dostat-na-ekonomickou-fakultu-1-dil-2/',
        'https://www.books.cz/chcete-se-dostat-na-pravnickou-fakultu-3/',
        # '', # pravnicka 2
        'https://www.books.cz/jak-se-dostat-na-vysokou-skolu-2/',
        'https://www.books.cz/zaklady-spolecenskych-ved-i-2/',
    ]

    PathBooks = {
        'BookStore' : 'Books.cz',
        #              /html/body/div[1]/div[2]/div/div[1]/div/div[2]/div[1]/div[2]/h1
        'name'      : '/html/body/div[1]/div[2]/div/div[1]/div/div[2]/div[1]/div[2]/h1',
        'url'       : '/html/body/div[1]/div[2]/div/div[1]/div/div[2]/div[1]/div[2]/div[2]/div/div[2]',
    }

    StockBooks = 'Skladem 5+'

# ----------- Levne-Knizky ---------- #
    UrlLK = [
        'https://www.levne-knizky.cz/studijni-predpoklady-a-zaklady-logiky-1-dil/',
        'https://www.levne-knizky.cz/studijni-predpoklady-a-zaklady-logiky-2-dil/',
        # '', # lekarska 1
        # '', # lekarska 2
        'https://www.levne-knizky.cz/chcete-se-dostat-na-lekarskou-fakultu-3-dil/',
        'https://www.levne-knizky.cz/chcete-se-dostat-na-lekarskou-fakultu-4-dil/',
        'https://www.levne-knizky.cz/chcete-se-dostat-na-fakultu-socialnich-studii-ved/',
        'https://www.levne-knizky.cz/chcete-se-dostat-na-vysokou-skolu-anglictina/',
        'https://www.levne-knizky.cz/chcete-se-dostat-na-vysokou-skolu-nemcina/',
        'https://www.levne-knizky.cz/chcete-se-dostat-na-ekonomickou-fakultu-1-dil/',
        'https://www.levne-knizky.cz/chcete-se-dostat-na-pravnickou-fakultu-2/',
        # '', # pravnicka 2
        'https://www.levne-knizky.cz/jak-se-dostat-na-vysokou-skolu/',
        'https://www.levne-knizky.cz/zaklady-spolecenskych-ved-i/',
    ]

    PathLK = {
        'BookStore' : 'Levne-Knizky',
        'name'      : '/html/body/div[2]/div[2]/div/div[1]/div/div[2]/div[1]/div[2]/h1',
        'url'       : '/html/body/div[2]/div[2]/div/div[1]/div/div[2]/div[1]/div[2]/div[2]',
    }

    StockLK = '5+'



class bookstores:
    iUrl = {
        'Dobrovsky'     : 'https://www.knihydobrovsky.cz/',
        'Kosmas'        : 'https://www.kosmas.cz/',
        'Luxor'         : 'https://www.luxor.cz/',
        'Martinus'      : 'https://www.martinus.cz/',
        'Megaknihy'     : 'https://www.megaknihy.cz/',
        'ABZ'           : 'https://knihy.abz.cz/',
        'Knihcentrum'   : 'https://www.knihcentrum.cz/',
        'Knihy'         : 'https://www.knihy.cz/',
        'Booktook'      : 'https://www.booktook.cz/',
        'Sevt'          : 'https://www.sevt.cz/',
        'Dumknihy'      : 'https://www.dumknihy.cz/',
        'Ladvi'         : 'https://www.knihkupectvi-ladvi.cz/',
        'Ucebnice'      : 'https://www.ucebnice.cz/',
        'Beletrie'      : 'https://www.beletrie.eu/',
        'Libristo'      : 'https://www.libristo.cz/',
        'Knizniarcha'   : 'https://www.knizniarcha.cz/',
        'Books.cz'      : 'https://www.books.cz/',
        'Levne-knizky'  : 'https://www.levne-knizky.cz/',
    }

    iEmails = {
        'Dobrovsky'     : 'poradime@knihydobrovsky.cz',
        'Kosmas'        : 'nakup@kosmas.cz',
        'Luxor'         : 'info@luxor.cz',
        'Martinus'      : 'naslovicko@martinus.cz',
        'Megaknihy'     : 'info@megaknihy.cz',
        'ABZ'           : 'knihy@abz.cz',
        'Knihcentrum'   : 'obchod@knihcentrum.cz',
        'Knihy'         : 'info@levne-knizky.cz',
        'Booktook'      : 'info@booktook.cz',
        'Sevt'          : 'kyncl@sevt.cz',
        'Dumknihy'      : 'eshop@kanzelsberger.cz',
        'Ladvi'         : 'info@knihkupectvi-ladvi.cz',
        'Ucebnice'      : 'info@ucebnice.cz',
        'Beletrie'      : 'obchod@beletrie.eu',
        'Libristo'      : 'info@libristo.cz',
        'Knizniarcha'   : 'obchod@knizniarcha.cz',
        'Books.cz'      : 'info@books.cz',
        'Levne-knizky'  : 'info@levne-knizky.cz',
    }
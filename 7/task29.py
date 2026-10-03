#todo: Взлом шифра
Вы знаете, что фраза зашифрована кодом цезаря с неизвестным сдвигом.
Попробуйте все возможные сдвиги и расшифруйте фразу.


grznuamn zngz cge sge tuz hk uhbouay gz loxyz atrkyy eua'xk jazin.

def caesar_decrypt(text, shift):
    result = ""
    for char in text:
        if char.isalpha():
            base = ord('A') if char.isupper() else ord('a')
            decrypted_char = chr((ord(char) - base - shift) % 26 + base)
            result += decrypted_char
        else:
            result += char
    return result


encrypted_phrase = "grznuamn zngz cge sge tuz hk uhbouay gz loxyz atrkyy eua'xk jazin."

print("Все возможные варианты расшифровки:")
print("=" * 60)

for shift in range(26):
    decrypted = caesar_decrypt(encrypted_phrase, shift)
    print(f"Сдвиг {shift:2d}: {decrypted}")

print("=" * 60)

вывод:


Все возможные варианты расшифровки:
============================================================
Сдвиг  0: grznuamn zngz cge sge tuz hk uhbouay gz loxyz atrkyy eua'xk jazin.
Сдвиг  1: fqymtzlm ymfy bfd rfd sty gj tgantzx fy knwxy zsqjxx dtz'wj izyhm.
Сдвиг  2: epxlsykl xlex aec qec rsx fi sfzmsyw ex jmvwx yrpiww csy'vi hyxgl.
Сдвиг  3: dowkrxjk wkdw zdb pdb qrw eh reylrxv dw iluvw xqohvv brx'uh gxwfk.
Сдвиг  4: cnvjqwij vjcv yca oca pqv dg qdxkqwu cv hktuv wpnguu aqw'tg fwvej.
Сдвиг  5: bmuipvhi uibu xbz nbz opu cf pcwjpvt bu gjstu vomftt zpv'sf evudi.
Сдвиг  6: although that way may not be obvious at first unless you're dutch.
Сдвиг  7: zksgntfg sgzs vzx lzx mns ad nauhntr zs ehqrs tmkdrr xnt'qd ctsbg.
Сдвиг  8: yjrfmsef rfyr uyw kyw lmr zc mztgmsq yr dgpqr sljcqq wms'pc bsraf.
Сдвиг  9: xiqelrde qexq txv jxv klq yb lysflrp xq cfopq rkibpp vlr'ob arqze.
Сдвиг 10: whpdkqcd pdwp swu iwu jkp xa kxrekqo wp benop qjhaoo ukq'na zqpyd.
Сдвиг 11: vgocjpbc ocvo rvt hvt ijo wz jwqdjpn vo admno pigznn tjp'mz ypoxc.
Сдвиг 12: ufnbioab nbun qus gus hin vy ivpciom un zclmn ohfymm sio'ly xonwb.
Сдвиг 13: temahnza matm ptr ftr ghm ux huobhnl tm ybklm ngexll rhn'kx wnmva.
Сдвиг 14: sdlzgmyz lzsl osq esq fgl tw gtnagmk sl xajkl mfdwkk qgm'jw vmluz.
Сдвиг 15: rckyflxy kyrk nrp drp efk sv fsmzflj rk wzijk lecvjj pfl'iv ulkty.
Сдвиг 16: qbjxekwx jxqj mqo cqo dej ru erlyeki qj vyhij kdbuii oek'hu tkjsx.
Сдвиг 17: paiwdjvw iwpi lpn bpn cdi qt dqkxdjh pi uxghi jcathh ndj'gt sjirw.
Сдвиг 18: ozhvciuv hvoh kom aom bch ps cpjwcig oh twfgh ibzsgg mci'fs rihqv.
Сдвиг 19: nygubhtu gung jnl znl abg or boivbhf ng svefg hayrff lbh'er qhgpu.
Сдвиг 20: mxftagst ftmf imk ymk zaf nq anhuage mf rudef gzxqee kag'dq pgfot.
Сдвиг 21: lweszfrs esle hlj xlj yze mp zmgtzfd le qtcde fywpdd jzf'cp ofens.
Сдвиг 22: kvdryeqr drkd gki wki xyd lo ylfsyec kd psbcd exvocc iye'bo nedmr.
Сдвиг 23: jucqxdpq cqjc fjh vjh wxc kn xkerxdb jc orabc dwunbb hxd'an mdclq.
Сдвиг 24: itbpwcop bpib eig uig vwb jm wjdqwca ib nqzab cvtmaa gwc'zm lcbkp.
Сдвиг 25: hsaovbno aoha dhf thf uva il vicpvbz ha mpyza buslzz fvb'yl kbajo.
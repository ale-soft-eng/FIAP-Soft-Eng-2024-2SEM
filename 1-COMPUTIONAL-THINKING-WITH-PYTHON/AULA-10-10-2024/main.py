def calcular_media_cp_challenge(cp1,cp2,challenge):
    media_cp = ((cp1 + cp2 + challenge) / 3) * 0.2
    return media_cp
print(calcular_media_cp_challenge(9, 7, 8))

def calcular_media_gs(nota_gs):
    media_gs = nota_gs * 0.8
    return media_gs
print(calcular_media_gs(95))

def calcular_media_semestral(media_cp, media_gs):
    media_semestral = media_cp + media_gs
    return media_semestral
print(calcular_media_semestral(1.6, 76))

def calcular_media_semestral_1(media_semestral, porcentagem=0.4):
    media_semestral_1 = media_semestral * porcentagem
    return media_semestral_1
print(calcular_media_semestral_1(77.6))

def calcular_media_semestral_2(media_semestral, porcentagem=0.6):
    media_semestral_2 = media_semestral * porcentagem
    return media_semestral_2



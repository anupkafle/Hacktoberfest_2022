from mcpi.minecraft import Minecraft
from time import sleep
mc = Minecraft.create()

#mc.settings('world_immutable',True)
    
#posicao inicial (nao modificar, base para construcoes)
mc.player.setTilePos(200,100,200)
pos = mc.player.getTilePos()
x=pos.x
y=pos.y
z=pos.z

#medidas das salas
largportas=14
altportas=5
compportas=10

largnether=6
altnether=5
compnether=6

largmorte=14
altmorte=5
compmorte=10

#variavel de blocos
ar=0
quartzo=155
bedrock=7
torch=89
tijolo=159,5
purpur=201
endstone=121
lanterna=169
lava = 213
vidro=20
esmeralda=133
teia=30
ouro=41
diamante=57
redstone=152

#####################CRIAÇÃO DE SALAS#####################
#sala_1
mc.setBlocks(x-1,y-1,z-1,x+largportas+1,y+altportas+1,z+compportas+1,bedrock)
mc.setBlocks(x,y,z,x+largportas,y+altportas,z+compportas,quartzo)
mc.setBlocks(x+1,y+1,z+1,x+largportas-1,y+altportas-1,z+compportas-1,ar)
mc.setBlock(x+4,y+1,z,ar)
mc.setBlock(x+4,y+2,z,ar)
mc.setBlock(x+7,y+1,z,ar)
mc.setBlock(x+7,y+2,z,ar)
mc.setBlock(x+10,y+1,z,ar)
mc.setBlock(x+10,y+2,z,ar)
mc.setBlock(x+4,y,z,ouro)
mc.setBlock(x+7,y,z,diamante)
mc.setBlock(x+10,y,z,redstone)
mc.setBlock(x+4,y+3,z,torch)
mc.setBlock(x+7,y+3,z,torch)
mc.setBlock(x+10,y+3,z,torch)
mc.setBlock(x+4,y+3,z+10,torch)
mc.setBlock(x+7,y+3,z+10,torch)
mc.setBlock(x+10,y+3,z+10,torch)

#sala_2
mc.setBlocks(x-1,y+10,z-1,x+largportas+1,y+altportas+12,z+compportas+1,bedrock)
mc.setBlocks(x,y+11,z,x+largportas,y+altportas+11,z+compportas,tijolo)
mc.setBlocks(x+1,y+12,z+1,x+largportas-1,y+altportas+10,z+compportas-1,ar)
mc.setBlock(x+4,y+12,z,ar)
mc.setBlock(x+4,y+13,z,ar)
mc.setBlock(x+7,y+12,z,ar)
mc.setBlock(x+7,y+13,z,ar)
mc.setBlock(x+10,y+12,z,ar)
mc.setBlock(x+10,y+13,z,ar)
mc.setBlock(x+4,y+11,z,ouro)
mc.setBlock(x+7,y+11,z,diamante)
mc.setBlock(x+10,y+11,z,redstone)
mc.setBlock(x+4,y+14,z,torch)
mc.setBlock(x+7,y+14,z,torch)
mc.setBlock(x+10,y+14,z,torch)
mc.setBlock(x+4,y+14,z+10,torch)
mc.setBlock(x+7,y+14,z+10,torch)
mc.setBlock(x+10,y+14,z+10,torch)

#sala_3
mc.setBlocks(x-1,y+20,z-1,x+largportas+1,y+altportas+22,z+compportas+1,bedrock)
mc.setBlocks(x,y+21,z,x+largportas,y+altportas+21,z+compportas,lanterna)
mc.setBlocks(x+1,y+22,z+1,x+largportas-1,y+altportas+20,z+compportas-1,ar)
mc.setBlock(x+4,y+22,z,ar)
mc.setBlock(x+4,y+23,z,ar)
mc.setBlock(x+7,y+22,z,ar)
mc.setBlock(x+7,y+23,z,ar)
mc.setBlock(x+10,y+22,z,ar)
mc.setBlock(x+10,y+23,z,ar)
mc.setBlock(x+4,y+21,z,ouro)
mc.setBlock(x+7,y+21,z,diamante)
mc.setBlock(x+10,y+21,z,redstone)
mc.setBlock(x+4,y+24,z,torch)
mc.setBlock(x+7,y+24,z,torch)
mc.setBlock(x+10,y+24,z,torch)
mc.setBlock(x+4,y+24,z+10,torch)
mc.setBlock(x+7,y+24,z+10,torch)
mc.setBlock(x+10,y+24,z+10,torch)

#sala_4
mc.setBlocks(x-1,y+30,z-1,x+largportas+1,y+altportas+32,z+compportas+1,bedrock)
mc.setBlocks(x,y+31,z,x+largportas,y+altportas+31,z+compportas,endstone)
mc.setBlocks(x+1,y+32,z+1,x+largportas-1,y+altportas+30,z+compportas-1,ar)
mc.setBlock(x+4,y+32,z,ar)
mc.setBlock(x+4,y+33,z,ar)
mc.setBlock(x+7,y+32,z,ar)
mc.setBlock(x+7,y+33,z,ar)
mc.setBlock(x+10,y+32,z,ar)
mc.setBlock(x+10,y+33,z,ar)
mc.setBlock(x+4,y+31,z,ouro)
mc.setBlock(x+7,y+31,z,diamante)
mc.setBlock(x+10,y+31,z,redstone)
mc.setBlock(x+4,y+34,z,torch)
mc.setBlock(x+7,y+34,z,torch)
mc.setBlock(x+10,y+34,z,torch)
mc.setBlock(x+4,y+34,z+10,torch)
mc.setBlock(x+7,y+34,z+10,torch)
mc.setBlock(x+10,y+34,z+10,torch)

#sala_5
mc.setBlocks(x-1,y+40,z-1,x+largportas+1,y+altportas+42,z+compportas+1,bedrock)
mc.setBlocks(x,y+41,z,x+largportas,y+altportas+41,z+compportas,purpur)
mc.setBlocks(x+1,y+42,z+1,x+largportas-1,y+altportas+40,z+compportas-1,ar)
mc.setBlock(x+4,y+42,z,ar)
mc.setBlock(x+4,y+43,z,ar)
mc.setBlock(x+7,y+42,z,ar)
mc.setBlock(x+7,y+43,z,ar)
mc.setBlock(x+10,y+42,z,ar)
mc.setBlock(x+10,y+43,z,ar)
mc.setBlock(x+4,y+41,z,ouro)
mc.setBlock(x+7,y+41,z,diamante)
mc.setBlock(x+10,y+41,z,redstone)
mc.setBlock(x+4,y+44,z,torch)
mc.setBlock(x+7,y+44,z,torch)
mc.setBlock(x+10,y+44,z,torch)
mc.setBlock(x+4,y+44,z+10,torch)
mc.setBlock(x+7,y+44,z+10,torch)
mc.setBlock(x+10,y+44,z+10,torch)

#sala_chance

mc.setBlocks(x+24,y-1,z-1,x+largmorte+26,y+altmorte+2,z+compmorte+1,bedrock)
mc.setBlocks(x+25,y,z,x+largmorte+25,y+altmorte+1,z+compmorte,quartzo)
mc.setBlocks(x+26,y+1,z+1,x+largmorte+24,y+altmorte,z+compmorte-1,ar)
mc.setBlocks(x+26,y+1,z+1,x+largmorte+24,y+1,z+compmorte-1,lava)
mc.setBlock(226,102,201,vidro)
mc.setBlock(228,102,204,vidro)
mc.setBlock(228,102,208,vidro)
mc.setBlock(231,102,207,vidro)
mc.setBlock(233,102,204,vidro)
mc.setBlock(236,102,202,vidro)
mc.setBlock(238,102,206,vidro)
mc.setBlock(238,102,209,esmeralda)

#salamorte
mc.setBlocks(x+24,y+9,z-1,x+largmorte+26,y+altmorte+12,z+compmorte+1,bedrock)
mc.setBlocks(x+25,y+10,z,x+largmorte+25,y+altmorte+11,z+compmorte,quartzo)
mc.setBlocks(x+26,y+11,z+1,x+largmorte+24,y+altmorte+10,z+compmorte-1,ar)
mc.setBlocks(x+26,y+11,z+1,x+largmorte+24,y+11,z+compmorte-1,lava)
mc.setBlocks(x+26,y+13,z+1,x+largmorte+24,y+14,z+compmorte-1,teia)

#sala_nether
mc.setBlocks(x+24,y+19,z-1,x+largmorte+26,y+altmorte+22,z+compmorte+1,bedrock)
mc.setBlocks(x+25,y+20,z,x+largmorte+25,y+altmorte+21,z+compmorte,bedrock)
mc.setBlocks(x+26,y+21,z+1,x+largmorte+24,y+altmorte+20,z+compmorte-1,ar)
mc.setBlock(x+29,y+24,z,torch)
mc.setBlock(x+32,y+24,z,torch)
mc.setBlock(x+35,y+24,z,torch)
mc.setBlock(x+29,y+24,z+10,torch)
mc.setBlock(x+32,y+24,z+10,torch)
mc.setBlock(x+35,y+24,z+10,torch)

def portalnether(x,y,z,blockType):
    return mc.setBlock(x,y,z,blockType)
portalnether(234,125,205,49)
portalnether(234,125,206,49)
portalnether(234,122,204,49)
portalnether(234,123,204,49)
portalnether(234,124,204,49)
portalnether(234,122,207,49)
portalnether(234,123,207,49)
portalnether(234,124,207,49)
portalnether(234,121,205,49)
portalnether(234,121,206,49)
portalnether(234,122,206,51)


mc.player.setTilePos(207,102,209)
sleep(1)

mc.postToChat('Leia tudo antes de comecar')
sleep(5)
mc.postToChat('Ola, bem vindo ao Escape dos Brother')
sleep(5)
mc.postToChat('Esse minigame ira definir onde sera sua origem no Minecraft')
sleep(5)
mc.postToChat('Nesta sala existem 3 portas')
sleep(5)
mc.postToChat('Cada porta tera uma surpresa')
sleep(5)
mc.postToChat('Podendo ser boa ou ruim')
sleep(5)
mc.postToChat('Boa sorte para iniciar sua aventura em Minecraft')
sleep(5)
mc.postToChat('Va no IDLE e digite seu nome')

nome=input('Digite seu nome: ')
mc.postToChat('Muito bem, '+ nome)
sleep(3)
mc.postToChat('Agora entre em uma das portas')
#######CONDICOES SALA 1#######
while True:
    sala1 = mc.player.getTilePos()
    xsala1=sala1.x
    ysala1=sala1.y
    zsala1=sala1.z
    blockBelow=mc.getBlock(xsala1,ysala1-1,zsala1)
    if blockBelow == ouro:
        mc.player.setTilePos(207,112,209)
        mc.postToChat('Muito bem, '+ nome +', voce chegou na segunda sala')
        sleep(1)
        mc.postToChat('Escolha outra porta e boa sorte')
        break
        
    elif blockBelow == diamante:
        mc.player.setTilePos(226,103,201)
        mc.postToChat('Ops, ' + nome + ', parece que voce caiu em meio a lava')
        mc.postToChat('Pule sobre os blocos de vidro')
        mc.postToChat('Vai filhaaao')
        while True:
            salalava = mc.player.getPos()
            xsalalava = salalava.x
            ysalalava = salalava.y
            zsalalava = salalava.z
            blockBelow1 = mc.getBlock(xsalalava,ysalalava-1,zsalalava)
            if blockBelow1 == lava:
                mc.player.setTilePos(226,103,201)
                mc.postToChat('Deu mole')
            elif blockBelow1 == esmeralda:
                mc.player.setTilePos(207,112,209)
                mc.postToChat('Muito bem, '+ nome +', voce chegou na segunda sala')
                sleep(1)
                mc.postToChat('Escolha outra porta e boa sorte')
                break
        break
    elif blockBelow == redstone:
        mc.player.setTilePos(233,114,205)
        mc.postToChat('Lamentavel uma morte tao lenta')
        mc.postToChat('Execute o codigo novamente')
        while True:
            salalava = mc.player.getPos()
            xsalalava = salalava.x
            ysalalava = salalava.y
            zsalalava = salalava.z
            blockBelow1 = mc.getBlock(xsalalava,ysalalava-1,zsalalava)
            if blockBelow1 == lava:
                mc.player.setTilePos(233,114,205)
        break
                
#######CONDICOES SALA 2#######
while True:
    sala1 = mc.player.getTilePos()
    xsala1=sala1.x
    ysala1=sala1.y
    zsala1=sala1.z
    blockBelow=mc.getBlock(xsala1,ysala1-1,zsala1)
    if blockBelow == diamante:
        mc.player.setTilePos(207,122,209)
        mc.postToChat('Muito bem, '+ nome +', voce chegou na terceira sala')
        sleep(1)
        mc.postToChat('Escolha outra porta e boa sorte')
        break
        
    elif blockBelow == ouro:
        mc.player.setTilePos(226,103,201)
        mc.postToChat('Ops, ' + nome + ', parece que voce caiu em meio a lava')
        mc.postToChat('Pule sobre os blocos de vidro')
        mc.postToChat('Vai filhaaao')
        while True:
            salalava = mc.player.getPos()
            xsalalava = salalava.x
            ysalalava = salalava.y
            zsalalava = salalava.z
            blockBelow1 = mc.getBlock(xsalalava,ysalalava-1,zsalalava)
            if blockBelow1 == lava:
                mc.player.setTilePos(226,103,201)
                mc.postToChat('Deu mole')
            elif blockBelow1 == esmeralda:
                mc.player.setTilePos(207,122,209)
                mc.postToChat('Muito bem, '+ nome +', voce chegou na terceira sala')
                sleep(1)
                mc.postToChat('Escolha outra porta e boa sorte')
                break
        break
    elif blockBelow == redstone:
        mc.player.setTilePos(233,114,205)
        mc.postToChat('Lamentavel uma morte tao lenta')
        mc.postToChat('Execute o codigo novamente')
        while True:
            salalava = mc.player.getPos()
            xsalalava = salalava.x
            ysalalava = salalava.y
            zsalalava = salalava.z
            blockBelow1 = mc.getBlock(xsalalava,ysalalava-1,zsalalava)
            if blockBelow1 == lava:
                mc.player.setTilePos(233,114,205)
        break
                
#######CONDICOES SALA 3#######
while True:
    sala1 = mc.player.getTilePos()
    xsala1=sala1.x
    ysala1=sala1.y
    zsala1=sala1.z
    blockBelow=mc.getBlock(xsala1,ysala1-1,zsala1)
    if blockBelow == ouro:
        mc.player.setTilePos(207,132,209)
        mc.postToChat('Muito bem, '+ nome +', voce chegou na quarta sala')
        sleep(1)
        mc.postToChat('Escolha outra porta e boa sorte')
        break
        
    elif blockBelow == redstone:
        mc.player.setTilePos(226,103,201)
        mc.postToChat('Ops, ' + nome + ', parece que voce caiu em meio a lava')
        mc.postToChat('Pule sobre os blocos de vidro')
        mc.postToChat('Vai filhaaao')
        while True:
            salalava = mc.player.getPos()
            xsalalava = salalava.x
            ysalalava = salalava.y
            zsalalava = salalava.z
            blockBelow1 = mc.getBlock(xsalalava,ysalalava-1,zsalalava)
            if blockBelow1 == lava:
                mc.player.setTilePos(226,103,201)
                mc.postToChat('Deu mole')
            elif blockBelow1 == esmeralda:
                mc.player.setTilePos(207,132,209)
                mc.postToChat('Muito bem, '+ nome +', voce chegou na quarta sala')
                sleep(1)
                mc.postToChat('Escolha outra porta e boa sorte')
                break
        break
    elif blockBelow == diamante:
        mc.player.setTilePos(233,114,205)
        mc.postToChat('Lamentavel uma morte tao lenta')
        mc.postToChat('Execute o codigo novamente')
        while True:
            salalava = mc.player.getPos()
            xsalalava = salalava.x
            ysalalava = salalava.y
            zsalalava = salalava.z
            blockBelow1 = mc.getBlock(xsalalava,ysalalava-1,zsalalava)
            if blockBelow1 == lava:
                mc.player.setTilePos(233,114,205)
        break

#######CONDICOES SALA 4#######
while True:
    sala1 = mc.player.getTilePos()
    xsala1=sala1.x
    ysala1=sala1.y
    zsala1=sala1.z
    blockBelow=mc.getBlock(xsala1,ysala1-1,zsala1)
    if blockBelow == redstone:
        mc.player.setTilePos(207,142,209)
        mc.postToChat('Parabens, '+ nome +', voce chegou na ultima sala')
        sleep(1)
        mc.postToChat('Escolha outra porta e boa sorte')
        break
        
    elif blockBelow == diamante:
        mc.player.setTilePos(226,103,201)
        mc.postToChat('Ops, ' + nome + ', parece que voce caiu em meio a lava')
        mc.postToChat('Pule sobre os blocos de vidro')
        mc.postToChat('Vai filhaaao')
        while True:
            salalava = mc.player.getPos()
            xsalalava = salalava.x
            ysalalava = salalava.y
            zsalalava = salalava.z
            blockBelow1 = mc.getBlock(xsalalava,ysalalava-1,zsalalava)
            if blockBelow1 == lava:
                mc.player.setTilePos(226,103,201)
                mc.postToChat('Deu mole')
            elif blockBelow1 == esmeralda:
                mc.player.setTilePos(207,142,209)
                mc.postToChat('Parabens, '+ nome +', voce chegou na ultima sala')
                sleep(1)
                mc.postToChat('Escolha outra porta e boa sorte')
                break
        break
    elif blockBelow == ouro:
        mc.player.setTilePos(233,114,205)
        mc.postToChat('Lamentavel uma morte tao lenta')
        mc.postToChat('Execute o codigo novamente')
        while True:
            salalava = mc.player.getPos()
            xsalalava = salalava.x
            ysalalava = salalava.y
            zsalalava = salalava.z
            blockBelow1 = mc.getBlock(xsalalava,ysalalava-1,zsalalava)
            if blockBelow1 == lava:
                mc.player.setTilePos(233,114,205)
        break
     
 #######CONDICOES SALA 5#######
while True:
    sala1 = mc.player.getTilePos()
    xsala1=sala1.x
    ysala1=sala1.y
    zsala1=sala1.z
    blockBelow=mc.getBlock(xsala1,ysala1-1,zsala1)
    if blockBelow == diamante:
        mc.player.setTilePos(-31,78,402)
        mc.postToChat(nome +', sua jornada se inicia agora')
        sleep(5)
        mc.postToChat('Boa sorte!')
        break
        
    elif blockBelow == redstone:
        mc.player.setTilePos(-183,35,-1204)
        mc.postToChat('Rapido, '+ nome +', suba para a superficie')
        sleep(10)
        mc.postToChat('Sua jornada acaba de iniciar, boa sorte!')
        break

    elif blockBelow == ouro:
        mc.player.setTilePos(226,121,205)
        sleep(2)
        mc.postToChat('O que aconteceu?? Onde estamos??')
        sleep(2)
        mc.postToChat('Este portal...')
        sleep(2)
        mc.postToChat('Nao temos opcao, '+ nome + ', entre nele')
        sleep(2)
        mc.postToChat('Iniciaremos no Nether, procure o portal em 46, 93, 42')
        break


def partida ():
  n = int (input ('Quantas peças? ')) # Número total de peças n.
  m = int (input ('Limite de peças por jogada? '))

  var = 1
  k = 0
  g = 0
# Pessoa: k = 1 e g = 0
# PC: k = 0 e g = 1 

  if n == m: 
    print ()
    print ('Computador começa!')
    if n == 1:
      print ()
      print ('O computador tirou uma peça.', 'Fim do Jogo! O computador ganhou!')
      #n = m
     
    elif n > 1:
      print ()
      print ('O computador tirou', m, 'peças.', 'Fim do Jogo! O computador ganhou!')
      #n = m

  imprime = False
      
  if n != m:
    if n < m:
      print ()
      print ('Oops! Jogada inválida! Tente de novo.')
      partida ()


    elif n > m: # else
      if n % (m + 1) == 0: # Pessoa.
        print ()
        print ('Você começa!')
        print ()
        var = usuario_escolhe_jogada (n, m) 

        if type (var) == int:
          n = n - var
          if var == 1:
            print ()
            print ('Você tirou uma peça', '\nAgora restam', n, 'peça(s) no tabuleiro.') 
            k = 0
            g = 1
          else:
            print ()
            print ('Você tirou', var, 'peças.', '\nAgora restam', n, 'peça(s) no tabuleiro.')
            k = 0
            g = 1
       
      else: # Computador
        print ()
        print ('Computador começa!')
        print ()
        var = computador_escolhe_jogada (n, m)
        n = n - var
        if var == 1:
          print ()
          print ('O computador tirou uma peça.', '\nAgora restam', n, 'peça(s) no tabuleiro.')
          k = 1
          g = 0
        else:
          print ()
          print ('O computador tirou', var, 'peças.', '\nAgora restam', n, 'peça(s) no tabuleiro.')
          k = 1
          g = 0
      
  while n > 0:
    
    if k == 1 and g == 0: # Pessoa
      var = usuario_escolhe_jogada (n, m)
      n = n - var
      k = 0
      g = 1

      if n > 0:
        if var == 1:
          print ()
          print ('Você tirou uma peça', '\nAgora restam', n, 'peça(s) no tabuleiro.')
          
        else:
          print ()
          print ('Você tirou', var, 'peças.', '\nAgora restam', n, 'peça(s) no tabuleiro.')
          
      elif n <= 0: 
        if var == 1:
          print ()
          print ('Você tirou uma peça.', 'Fim do Jogo! Você ganhou!')
          imprime = True # pessoa
          #break
        else:
          print ()
          print ('Você tirou', var, 'peças.', 'Fim do Jogo! Você ganhou!')
          imprime = True
          #break
    
    elif k == 0 and g == 1: # Pc
      var = computador_escolhe_jogada (n, m)
      n = n - var
      k = 1
      g = 0

      if n > 0:
        if var == 1:
          print ()
          print ('O computador tirou uma peça.', '\nAgora restam', n, 'peça(s) no tabuleiro.')
          
        else:
          print ()
          print ('O computador tirou', var, 'peças.', '\nAgora restam', n, 'peça(s) no tabuleiro.')
          
      elif n <= 0:
        if var == 1:
          print ()
          print ('O computador tirou uma peça.', 'Fim do Jogo! O computador ganhou!')
          #print ()
          #rint ('O Computador ganhou!')
          imprime = False
          #break
        else:
          print ()
          print ('O computador tirou', var, 'peças.', 'Fim do Jogo! O computador ganhou!')
          #print ()
          #print ('O computador ganhou!')
          imprime = False
          #break

  if imprime == True:
    return True # pessoa
  elif imprime == False:
    return False # pc

def computador_escolhe_jogada (n, m):
  ind = False
  t = 1
  while t <= m:
    d = n - t
    if d % (m + 1) == 0:
      ind = True
      var = t
    t += 1
  if ind:
    if var == 1:
      return var
    else:
      return var
  elif ind == False:
    var = m
    return var

def usuario_escolhe_jogada (n, m):
  if m < n: # n > m 
    print ()
    t = int (input ('Quantas peças você vai tirar? '))
    if 1 <= t <= m:
      var = t
      if var == 1:
        return var
      elif m >= var > 1:
        return var
    else:
      while t > m or t < 1:
        print ('Oops! Jogada inválida! Tente de novo.')
        t = int (input ('Quantas peças você vai tirar? '))
        var = t
      return var


        #usuario_escolhe_jogada (n, m)

  else:
    #a = 1
    #b = 0 
    while n <= m:
      print ()
      print ('Oops! Jogada inválida! Tente de novo.')
      #a = 1
      #b = 0

      #print ('O número de peças é:', n)
      a = int (input ('Quantas peças? '))
      b = int (input ('Limite de peças por jogada? ')) # m
      if a <= b:
        q = a
        o = b
        usuario_escolhe_jogada (q, o)
      elif a > b:
        var = usuario_escolhe_jogada (a, b)
        return var

def campeonato ():
  n = 0
  a = 0
  b = 0 
  while n < 3:
    t = partida()
    if t == True:
      print ('Você ganhou!')
      print ()
      a = a + 1
    elif t == False:
      print ('O computador ganhou!')
      print ()
      b = b + 1
    n += 1
  return print ('**** Final do campeonato! ****', '\n','\nPlacar: Você', a, 'x', b, 'Computador')

print ()
print ('Bem-vindo ao jogo do NIM! Escolha: ')
escolha = 0
while escolha != 1 or escolha != 2:
  print ()
  escolha = int (input ('1 - para jogar uma partida isolada \n2 - para jogar um campeonato! '))
  if escolha == 1:
    print ()
    print ('Você escolheu uma partida isolada!')
    break
  elif escolha == 2:
    print ()
    print ('Você escolheu um campeonato!')
    break
  else:
    print ()
    print ('Você escolheu uma opção inválida. Tente novamente!')

if escolha == 2:
  campeonato ()
elif escolha == 1:
  partida ()

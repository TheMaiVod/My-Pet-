#регистрация пользователя 
print('Добро пожаловать. Пожалуйста, пройдите регистрацию')
print('Кто вы: владелец питомца или желаете завести домашнее животное?')
regis=0
if regis==0:
    otv=str(input())
    #если есть питомец 
    if otv=='Владелец питомца':

    
        x=0
        for i in range (x,2):   
            if x==0:
                print('Как вас зовут?')
                user_name = str(input())
                print('Как зовут вашего питомца?')
                pet_name = str(input())
                print('Сколько лет вашему маленькому другу?')
                pet_old = str(input())
                if user_name=='' or pet_name =='' or pet_old=='':
                    x=0
                else:
                    print('Итак, ваше имя',user_name,'Вашего питомца зовут',pet_name,' и его возраст ', pet_old,'. Все данные верны?')
                    erw=str(input())
                    if erw=='Да':
                        x=1
                    else:
                        x=0    
            
        if x==1:
            print ('Расскажите о своем питомце поподробнее. Какая у него порода?')
            uspet=str(input())
            print ('А какого пола ваша заверушка?')
            uspet= uspet+str(input())
            print ('Ваш питомец:', pet_name,', ', uspet, 'возраст:', pet_old)
            
            regis=1
              
            
 
    #если нет питомца            
    if otv=='Хочу завести ':
        y=0
        if y==0:
            print('Как вас зовут?')
    
            user_name = str(input())
            if user_name=='':
                y=0
            else:
                y=1
        if y ==1:
            print(user_name,',Вы уже определились с выбором маленького друга?')
            vbr=str(input())
            if vbr=='Да':
                print('И на кого же пал ваш выбор?')
                vbr1=str(input())
                print(' Что же, это хороший выбор. мы предлагаем вам посмотреть в нашем приложении, в каком питомнике и по какой цене')
            else:
                print('Тогда посмотрите , что наше приложение сможет вам предложить. Надеемся, что вы сможете найти себе домашнюю зверушку. Помните: мы в ответе за тех, кого приручили.')
                regis=1
if regis==1:            
    print('Поздравляем, регистрация завершена')        
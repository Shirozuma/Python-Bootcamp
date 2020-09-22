# Sohini Mukhopadhyay
print("**********************************************************")
print("**********************************************************")
print("\t\t\tWELCOME TO FUTURE NATION")
print("**********************************************************")
print("What's your Name, oh you Future Seeker?")
name = input("My Name is: ")
print("Very Well, %s, May we know your Birth Sign?" %name)
flag=1
while flag==1:
    # MENU TO CHOOSE ZODIAC SIGN 
    print("\nChoose one of these-")
    print("1. Aries")
    print("2. Taurus")
    print("3. Gemini")
    print("4. Cancer")
    print("5. Leo")
    print("6. Virgo")
    print("7. Libra")
    print("8. Scorpio")
    print("9. Sagittarius")
    print("10. Capricorn")
    print("11. Aquarius")
    print("12. Pieces")
    sign = int(input("My sign is number: "))
    if 1<=sign<=12:
        flag = 0                                                  #input validation of correct sign
    else:
        print("\nAre you sure you chose the correct sign?")
        print("Please choose again")
        helpme = int(input("Do you need help to know your birth sign? Press 1 for Yes or 0 for No: "))
        if helpme == 1:                                           #helping to find zodiac sign
            flag2=1
            while flag2==1:                                       # for input validation of correct date and month
                date = int(input("Enter your date of birth: "))
                month = input("Enter your birth month: ")
                # month validation and date validation
                if month=="january":
                    if 0<date<20:
                        print("Your sign is Capricorn")
                        sign=10
                        flag=0
                        flag2=0
                    elif 19<date<32:
                        print("Your sign is Aquarius")
                        sign=11
                        flag=0
                        flag2=0
                    else:
                        print("Invalid date")
                elif month=="february":
                    if 0<date<20:
                        print("Your sign is Aquarius")
                        sign=11
                        flag=0
                        flag2=0
                    elif 19<date<30:
                        print("Your sign is Pieces")
                        sign=12
                        flag=0
                        flag2=0
                    else:
                        print("Invalid date")
                elif month=="march":
                    if 0<date<21:
                        print("Your sign is Pieces")
                        sign=12
                        flag=0
                        flag2=0
                    elif 20<march<32:
                        print("Your sign is Aries")
                        sign=1
                        flag=0
                        flag2=0
                    else:
                        print("Invalid date")
                elif month=="april":
                    if 0<date<21:
                        print("Your sign is Aries")
                        sign=1
                        flag=0
                        flag2=0
                    elif 20<date<31:
                        print("Your sign is Taurus")
                        sign=2
                        flag=0
                        flag2=0
                    else:
                        print("Invalid date")
                elif month=="may":
                    if 0<date<21:
                        print("Your sign is Taurus")
                        sign=2
                        flag=0
                        flag2=0
                    elif 20<date<32:
                        print("Your sign is Gemini")
                        sign=3
                        flag=0
                        flag2=0
                    else:
                        print("Invalid date")
                elif month=="june":
                    if 0<date<21:
                        print("Your sign is Gemini")
                        sign=3
                        flag=0
                        flag2=0
                    elif 20<date<31:
                        print("Your sign is Cancer")
                        sign=4
                        flag=0
                        flag2=0
                    else:
                        print("Invalid date")
                elif month=="july":
                    if 0<date<23:
                        print("Your sign is Cancer")
                        sign=4
                        flag=0
                        flag2=0
                    elif 22<date<32:
                        print("Your sign is Leo")
                        sign=5
                        flag=0
                        flag2=0
                    else:
                        print("Invalid date")
                elif month=="august":
                    if 0<date<23:
                        print("Your sign is Leo")
                        sign=5
                        flag=0
                        flag2=0
                    elif 22<date<32:
                        print("Your sign is Virgo")
                        sign=6
                        flag=0
                        flag2=0
                    else:
                        print("Invalid date")
                elif month=="september":
                    if 0<date<23:
                        print("Your sign is Virgo")
                        sign=6
                        flag=0
                        flag2=0
                    elif 22<date<31:
                        print("Your sign is Libra")
                        sign=7
                        flag=0
                        flag2=0
                    else:
                        print("Invalid date")
                elif month=="october":
                    if 0<date<23:
                        print("Your sign is Libra")
                        sign=7
                        flag=0
                        flag2=0
                    elif 22<date<32:
                        print("Your sign is Scorpio")
                        sign=8
                        flag=0
                        flag2=0
                    else:
                        print("Invalid date")
                elif month=="november":
                    if 0<date<22:
                        print("Your sign is Scorpio")
                        sign=8
                        flag=0
                        flag2=0
                    elif 21<date<31:
                        print("Your sign is Sagittarius")
                        sign=9
                        flag=0
                        flag2=0
                    else:
                        print("Invalid date")
                elif month=="december":
                    if 0<date<22:
                        print("Your sign is Sagittarius")
                        sign=9
                        flag=0
                        flag2=0
                    elif 21<date<32:
                        print("Your sign is Capricorn")
                        sign=10
                        flag=0
                        flag2=0
                    else:
                        print("Invalid date")
                else:
                    print("Invalid Month")

# HOROSCOPE OF EVERY SIGN          
if sign==1:
    print("Oh my, an ARIES")
    print("\tCareer horoscope 2020 is indicating progress for Aries. The reason for this is that the lord of the 10th house of your zodiac sign is Saturn, which represents the karmic goodwill and fairness in a person. Saturn is making auspicious circumstances in the 9th house at the beginning of the year, then in the early days of the year, Saturn changes the place and occupies the 10th place. It can bring you plenty of opportunities to prove your talent and you should grab it. Overall, if you have worked hard, this could prove to be a year with achievements. This year will also be good for the people who are interested in starting their own business.")
elif sign==2:
    print("Oh my, a TAURUS")
    print("\tCareer Horoscope 2020 for Taurus Zodiac signals that this year is going to bring you challenges in terms of career. However, Saturn of the 10th house will create opportunities for you. At the end of the first quarter of the year, Saturn and Jupiter will move into your 9th house. The combination of Saturn and Jupiter will bring you many opportunities. At this time you can get good advice from friends, and from close relatives regarding your career. You will get the benefit of favorable circumstances at this time and success in your career will be created.")
elif sign==3:
    print("Oh my, a GEMINI")
    print("\tAccording to Career Horoscope 2020, this year is going to be very good for you in terms of career. Business or job opportunities are going to be flowing for you from all areas. This year will also enhance your status among others and there will be a significant increase in salary for the employed people. For those who have long been preparing for competitive exams and wanting to get jobs in any government sector, this year, you will find success. This is going to be a good year for those who are looking for a job in the education sector.  The presence of  Sun and Mercury in the 7th house at the beginning of the year is creating auspicious results. Along with these, Jupiter, which is the lord of the 5th house and is also present in the 7th house. Overall, these conditions can bring great opportunities for you in the education sector.")
elif sign==4:
    print("Oh my, a CANCER")
    print("\tAccording to the Career Horoscope 2020, this year you are seeing the full potential of success. For those who are interested in military services, information technology, science, media, cinema, hardware, etc. this year is likely to be a year of great results in their career. This year you can also get success in competitive examinations. For the people who are preparing for a government job, this year can bring achievements. This year you can get new opportunities to showcase your talent. However, success will only kiss your feet if you take that step further. You are not going to get anything by sitting and wondering about them, you will get results according to your hard work. Especially in the case of building a career, you will have to put on the efforts. The hard work you have done in the past can also get the results.")
elif sign==5:
    print("Oh my, a LEO")
    print("\tAccording to the Career Horoscope 2020, for the Leo Zodiac, the new year will prove to be your year. This year you are going to be full of excitement and enthusiasm, on the basis that you can maintain your dominance over your opponents. There is tremendous potential for job-seekers in their stature, rank, and salary. For those who want to start something new, this year can also be expected to be very successful. Especially in the fields of Iron, Electricity, Communication, and Technology, you can earn good profits.")
elif sign==6:
    print("Oh my, a VIRGO")
    print("\tAccording to the Virgo Career Horoscope 2020, you can expect to be progressive in your career. Natives who are of the working class will stand a chance to be promoted this year and new business opportunities will emerge for business people. You can work on new plans this year. Those people who want to start their own business can also expect this year to be very profitable for a startup. Although the beginning of the year may be a bit slow for you, you will be able to see the success throughout the year.")
elif sign==7:
    print("Oh my, a LIBRA")
    print("\tThe Libra Career Horoscope 2020 indicates that this year you are going to achieve a new high in your career. The presence of the moon in the 10th house is indicating to be very good in the year’s horoscope, which will show new opportunities in your career. Some good offers can also come this year. You are also going to work very hard, resulting in new responsibilities, new achievements. There will be an overall increase in your rank, status, and salary when you will work with full concentration. The idea of ??changing jobs will also come to mind but you have to control them, you can get good growth even after staying in one place. In fact, Saturn's vision is falling on the moon, which can leave your mind distracted but you need to think thoroughly before taking any steps.")
elif sign==8:
    print("Oh my, a SCORPIO")
    print("\tAccording to the Scorpio Career Horoscope 2020, this year is going to be very successful in the case of your career because the lord of the 11th house of your zodiac, the Sun in the year 2020, is creating auspicious changes which will bring success for you. Chances of promotion this year are also being made for employed people. Those people who have been struggling to coordinate with their seniors for some time may also have good relations with them")
elif sign==9:
    print("Oh my, a SAGITTARIUS")
    print("\tThe lord of career, Mercury is creating Beneficial outcomes will be experienced in this year's horoscope, will give you the opportunity to excel at your workplace. There will be achievements in the business world too. CHances of success in securing government jobs will also be created. The presence of Jupiter in the zodiac sign is creating beneficial results for you. By this, in the horoscope, you will find new energy within you and you will perform well at the workplace. Due to the presence of  Jupiter in the 7th place of your zodiac, none of you weaknesses and shortcomings will be persistent in front of others and this will benefit you. Any weaknesses inside you can not come in front of anyone. You can take advantage of this opportunity to overcome your shortcomings and move forward in your career.")
elif sign==10:
    print("Oh my, a CAPRICORN")
    print("\tAccording to the Capricorn Horoscope 2020, new opportunities will be available in the career of Capricorn people this year. You will get new opportunities. There can be a good success in the business world, especially for those who are associated with fashion, make-up, designing, garments, etc. will also have the advantage of getting success. The presence of five planets together in 12th position from your zodiac sign is in some ways harmful for you, but it is beneficial for your career. If you are into a business then you will benefit. Those who want to expand their business to foreign countries will get a chance. Those who work in the field of import-export can get success.")
elif sign==11:
    print("Oh my, an AQUARIUS")
    print("\tAccording to the Career Horoscope of 2020, this year will be very good for Aquarians. With the presence of Mars in the 10th house, there will be new possibilities for you. Those who are employed in the IT sector will have success in their fields. Those who are interested in government jobs can fulfill their wish as they will succeed in scoring well.")
elif sign==12:
    print("Oh my, a PIECES")
    print("The Career Horoscope 2020 of Pisces suggest that there will be new opportunities for your career . Especially for business people, this year is going to be celebratory because of the movement of planets 10th house to 11th will give auspicious results. Due to this there is a huge potential of profit and success. In accordance with the horoscope of 2020 this year, Mercury, Jupiter, Sun, Saturn, and Ketu are in place of karma with your zodiac sign. With this effect, you will get many opportunities to take your career to a new dimension this year. You should take advantage of that. If you are thinking of doing something new in the business world, then here you will get immense success. At this time if you plan to invest in a new business, you are more likely to get benefits. ")
else:
    print("How did you exit the loop without telling your correct Horoscopic Sign?")
    print("Are you a Wizard as well?!")
print("\n\n\tTHANKS FOR VISITING")
print("**********************************************************")
print("**********************************************************")


def generator(arr):
    wrongCounter = 0;
    checker = 0;
    index = 0;
    while( True ):
        for b in range(checker, len(arr) - 1):
            for c in range(len(arr[checker])):
                if( arr[checker][c] != arr[b+1][c] ):
                    wrongCounter += 1;
                    index = c;
            if wrongCounter == 1:
                result = arr[checker][:index] + arr[checker][(index+1):]
                return result;
            wrongCounter = 0;
            index = 0;
        checker += 1;


print(generator(["vtnihorkulbfvjcyzmsjgdxplw",
"vtnihorvujbfejcyzmsqgdlpaw",
"vtnihoriulbzejcyzmsrgdxpaw",
"vtsihowkulbfejcyzmszgdxpaw",
"vtnizorkunbfejcyzmsqgdypaw",
"vtnihorkdlbfojcyzmsqgdfpaw",
"vtpioorkulbfejcysmsqgdxpaw",
"vtnvhorkulbfhjcyzmsqgdipaw",
"vtrihorkylbaejcyzmsqgdxpaw",
"vtnigorkulbfejcyzmszgjxpaw",
"rtnihorkklbfejcyzmslgdxpaw",
"vtnihorkqlbfejcyzmsqgmppaw",
"vgnisorkulbfejcyzmsqgdkpaw",
"atnihorkulbfejcyzmdbgdxpaw",
"vtnihorkulbfejcezmsqqixpaw",
"vtnihorkucbfejcxzmsqgdypaw",
"vtnihorkulxfajcyzmsqgyxpaw",
"vbnihorkulbfescyzmsqgdxpae",
"vanshorkulbfejcyzjsqgdxpaw",
"vtnihoukulbfejcyzmwqgdxpbw",
"vtndhorkulbfejcyxmgqgdxpaw",
"ztnihlrkupbfejcyzmsqgdxpaw",
"vtoihkrkulbfejhyzmsqgdxpaw",
"vtnihorkalbiejcyzmsqgdxeaw",
"vtnihorhulcfejcyzqsqgdxpaw",
"vtnshotkulbfejcyzmsqvdxpaw",
"vtnihoryulbfejcyzmsqgpspaw",
"vtnihorkukbfmjcyzmsqgdxpcw",
"vtnihorkulbfejcybmsqgdupxw",
"vlnihorkulbfejcyzmsqgdmpac",
"vtnihorkulbfejcezmfqgdkpaw",
"vpnihorkulbfejcyzmsqfdxyaw",
"vtnihorkulbjejcysmcqgdxpaw",
"vdnihorkulffejcyzisqgdxpaw",
"vtnihorkulkfsjcyzrsqgdxpaw",
"vtnihorkulqfegoyzmsqgdxpaw",
"vtnihorkulbfeyhyzgsqgdxpaw",
"vnnihorkulbfejcyzmdqgdxpfw",
"vtnihorkulstejcyzmsqgdxpak",
"vtnphorkujbfejcczmsqgdxpaw",
"vtpihorkulbfejcyzmskgdxiaw",
"vtnihorkulbfejcdzmxqsdxpaw",
"vtnihorgulbfticyzmsqgdxpaw",
"veniuorkulbfejcyzmsqgdmpaw",
"vhnihorkclbfejyyzmsqgdxpaw",
"vtnihorkulbfejcyzmrqgsrpaw",
"dtnihorkzlhfejcyzmsqgdxpaw",
"vtnizorkulbfejcyzhsqgdxdaw",
"vtnihohkulbfejcybmpqgdxpaw",
"vtnihbrzulbfejcyzmsqgdppaw",
"stnihorkulmfejcyzmsqgdxeaw",
"vtnihorkulbfejmgzwsqgdxpaw",
"vtnihcrkulbfnjdyzmsqgdxpaw",
"vxxihorkulbfejcyzmsqddxpaw",
"vtnhhorkulbfejcyzmsqgdpiaw",
"vtnihoakulbfvjcyzmmqgdxpaw",
"vtbbhorkulbfejcyqmsqgdxpaw",
"vtnihnukulbfejcxzmsqgdxpaw",
"vteihorgulkfejcyzmsqgdxpaw",
"vbnihorkulbfejcyzmsqgdxpmt",
"itnihorkulbuejcyzmsqgdxpxw",
"vtnfhqrkulbfejcwzmsqgdxpaw",
"vtnihorkubbfedcyzmsqpdxpaw",
"rtnihorkulhfejcyzmsqgdxpah",
"vtnihorzulbfejcyqmsqqdxpaw",
"vtnihorkulbfeecyzmsqgdcgaw",
"vtniuorkulbfejpyzmsqxdxpaw",
"vtnicorkilbfajcyzmsqgdxpaw",
"vtzihorkulbfejcyzmsqgaxpkw",
"vtnihomkulbfejcyzmsqgvmpaw",
"vznihockulbfejcyzmsqgdjpaw",
"vtqmhorkulhfejcyzmsqgdxpaw",
"ptnihorkulbfsjcyzbsqgdxpaw",
"ftnihorkulbfejcepmsqgdxpaw",
"vtnhhorkulbfejyyzxsqgdxpaw",
"vtnihorkulbfejcyzmsiwdxpxw",
"vtnikorkulbfejvyzmnqgdxpaw",
"vtnihorkulbgejoyzmsqhdxpaw",
"vtnihorkulbwejqylmsqgdxpaw",
"vtnihorkdlbfejcyzwsqgdrpaw",
"vtnihorkulbfojcyzmtugdxpaw",
"vtnihonkulbtejcyzxsqgdxpaw",
"vtnihorkulrfevcyzmsqgdxpcw",
"vtnioorkulbfejcynmsqgdxpad",
"vtnihorkudffejcyzhsqgdxpaw",
"vtnihorkelbfejcqzmsqgdxbaw",
"jtnihokkulbfejcyzmsqgdrpaw",
"ztnihorrulbfejcyzlsqgdxpaw",
"vtwiforkulbfejcyzmsqpdxpaw",
"vtnihopvulbfejcyzmsqgzxpaw",
"vtnihzrkulafejcyzmsqgdxpaj",
"vtnixoekulbfejcyzmsqgdxpak",
"vtnihorkulbfejxyzmsqgdxhlw",
"vtnihorkulbfwjcyzmmqcdxpaw",
"vtnihorkulbfejcywmsdgdxzaw",
"vtnihorkulbfejfyzmsqggxuaw",
"vtnihnrkurbfejcyzmsqggxpaw",
"vtuihorkulbkejcyzmsqgdxpww",
"vtnihoriuljfejcyzssqgdxpaw",
"vtnihorkulyftjcezmsqgdxpaw",
"vtnihorkklbfeccyzmsqgdppaw",
"vtnihorkulbfdpcyzmsqgdxpcw",
"vtnihqrkulgfejcyzmeqgdxpaw",
"vtnihorktlbfejdyzmswgdxpaw",
"vinihzrkulbfeacyzmsqgdxpaw",
"vtuihorkupbfejcyzmsqgdxplw",
"vtnihorkulbfcjcyzmlqgdxpsw",
"vtnihorkllbfejcyzmsqgdxvak",
"qtnihorkulbfdjcyzusqgdxpaw",
"vtniherkulbhejcyzmsqgzxpaw",
"vtnzhorgulbfejcyzmsqgdxpew",
"vtnihoykulhfjjcyzmsqgdxpaw",
"vtnihookulyfejcyzmsqgdxqaw",
"jtnihorkulbfejcyzmssgdxpaq",
"vtnicorkulwfejcyzmsxgdxpaw",
"wtnihorkuubfejcyzmsqgdxpam",
"vtnihorkuggfejcyzmsdgdxpaw",
"vtnihurkulbfgjcyzmsqrdxpaw",
"ptnihorkuabfejcyzmsqgqxpaw",
"vtrihoykulbfejcyzmsqgdxpam",
"otnihorkulbfejcyzmpqgdxpjw",
"vtyihorkulbfejdyznsqgdxpaw",
"vtnihornulbfrjcizmsqgdxpaw",
"vtnihfrlulbfejcyzmsqgdxpah",
"atnihorkulbfejcyossqgdxpaw",
"vtnihorkuljfejcyzysqgdxpow",
"vtniyorkulbfejcyzmsqgdxbaz",
"venihorkulbfejctzmqqgdxpaw",
"vtrihorkulbfejcyjmsqgdxpfw",
"venitorkulbfexcyzmsqgdxpaw",
"vtbihorkulbfejcyzmwqgdxpyw",
"vtnihorkuubfejxyzmsqgdxkaw",
"vtqihorkulbnejcyzmsqgdxnaw",
"vteihorkurbfejcyzmsqwdxpaw",
"vtgjhorkxlbfejcyzmsqgdxpaw",
"ytniworkulbfejcyzmsqgdxptw",
"vtnihorkulbfejcyzmsvgixhaw",
"dtnihorkusbfejcyzmsqidxpaw",
"vtnihurkulbfejcdzmkqgdxpaw",
"vtgihorkulbfejcyzhsqgdxpaf",
"vtniudrkulbfeacyzmsqgdxpaw",
"vtnihorkulbfejcyemsokdxpaw",
"vtnihorkulbfejcyjmwqgdxpag",
"vtnihorpulbfetcpzmsqgdxpaw",
"ctnzhorkulbfejcyzmfqgdxpaw",
"vanihorkuhbwejcyzmsqgdxpaw",
"vtnihonkurbfejcyzvsqgdxpaw",
"vtnihgrkulbcejcbzmsqgdxpaw",
"vtnihorkutbfeacyzmsqcdxpaw",
"vtniaorkuhbfqjcyzmsqgdxpaw",
"vtnihorkylbfozcyzmsqgdxpaw",
"vtnihorkulbfejcypmfqgdxpbw",
"vtrphonkulbfejcyzmsqgdxpaw",
"vtnihorkulbdejcywmsqydxpaw",
"vtnikorkulbfejvyzknqgdxpaw",
"vznihorkulbfejcyzmsqbdxpam",
"vtmghorkulbfejcyzmsqghxpaw",
"vtnihorkulbfejcyzmshglxpfw",
"vtiihorkulbfejcjzmsqgdxoaw",
"rtnihorkulbfejcuzmsqgdxpow",
"vtnthoikulbuejcyzmsqgdxpaw",
"vtniholkulbfcjcyzmsqgdxpvw",
"vdnihorkulbbejcyzmsqgdxdaw",
"ntnihorkulbfojcyzmsqgdxzaw",
"vtniqorkulbfejcyzklqgdxpaw",
"vtnihorkulhfejcpzmsqgdxprw",
"vhnihorkulqfejcyzmsqgdapaw",
"vtnihorkolafejcyzmsqadxpaw",
"vtnihorkulbpejcyzasqgtxpaw",
"vtnihgiyulbfejcyzmsqgdxpaw",
"dtnihorkulbffjcyzmsqgdfpaw",
"vtnvhorhulbfejcyzmpqgdxpaw",
"vtniholkulbfebcyzmsqgnxpaw",
"vunihorkulbbejcyznsqgdxpaw",
"vtnihorkulbfehcyomsqgaxpaw",
"vtnihorkllboejcyzmsigdxpaw",
"vtnihwrkulbfejcywmsqgdxiaw",
"vtnoherkulbfbjcyzmsqgdxpaw",
"vtnbhorkulbfejcyzmsqgkxpaa",
"vtnihorkilbfdjxyzmsqgdxpaw",
"vtnfhorkuvbfejcyzmsqgixpaw",
"vtnyhorkulbpejcyzmsqgdxjaw",
"vtnihomkalbfejcyzmqqgdxpaw",
"vtnihorkulbfejcybmsqgjxvaw",
"vtnihorkulbfgjcnzmsqbdxpaw",
"vtnihorkulbfejcyzmpqgsxpap",
"lmnihorkulbfejcizmsqgdxpaw",
"vtmahkrkulbfejcyzmsqgdxpaw",
"vtnihorkulbfujcyrcsqgdxpaw",
"vtnzhorkulbfejcyzjvqgdxpaw",
"vtnicorkulbfejmyzmsqgdxvaw",
"vtnyhojkulbfejcyzmsngdxpaw",
"vtnuhorkulbfejcyzlsqgdxpmw",
"vtnihorkulufejcgzmtqgdxpaw",
"vtnihfrkulbfejnyzmsigdxpaw",
"vtnzhorkulbdejnyzmsqgdxpaw",
"vttihorkulbfejcyzmyqgdxwaw",
"vknihorkulbfejnylmsqgdxpaw",
"vtnihorkulbfejcfrmsqgdxpaz",
"vtnchormulbfejcyzmsqgdopaw",
"vtnihorkulbfebcyzusqgdxpam",
"jtnihorwulbfejcyzksqgdxpaw",
"ctnihodkutbfejcyzmsqgdxpaw",
"vonihorkultfejcyzmsqgixpaw",
"vtnihorkulbqejcyzmsqgdypcw",
"vfnihorkulbfbjcyzmsqcdxpaw",
"utnihorkulbfejcyqmsqgdxraw",
"vtnihorkjllfejcyzmskgdxpaw",
"vtnihorkulbfejcyvisqgdapaw",
"vtnihorkclzfejcyzmsqvdxpaw",
"vtnihwrkvlffejcyzmsqgdxpaw",
"vtnihlrkulbfejcrzmsqydxpaw",
"vtnihorkulbfbjtysmsqgdxpaw",
"vtnihorkulbfxjcepmsqgdxpaw",
"ttnihorkulbfejpyzmsqgdxpaz",
"vtnwhorkolbfejcdzmsqgdxpaw",
"vtnihorkulbfejcyzdsqgdxppn",
"vtnwporkulbfercyzmsqgdxpaw",
"vtnshorxuvbfejcyzmsqgdxpaw",
"vtnihxrkulbfejcyomsqfdxpaw",
"vtnwhorkrljfejcyzmsqgdxpaw",
"vqnihorkulbfejcyzmtqgdxpuw",
"vtnnhorkulbfhrcyzmsqgdxpaw",
"vtuihwrkulbfedcyzmsqgdxpaw",
"vtgbhorkucbfejcyzmsqgdxpaw",
"vtnitorkulbfejcozmsqgdkpaw",
"otnihomkulbfejcyzmsqgdxhaw",
"vtnihgrkulbfrjcyzmsqxdxpaw",
"vtnihorkulbfujcyzmsqghxpzw",
"vsnihopkhlbfejcyzmsqgdxpaw",
"vtniherkulbfejcyzmpzgdxpaw",
"vtnxhorkulbfejcszmsqgdxcaw",
"vtnihorkulbfejctzmsxadxpaw",
"vtnihorkslbmejcyzmsqgnxpaw",
"vtnwhorgulbfegcyzmsqgdxpaw",
"vtnihorkulbfsjcyzmsqgdxiau",
"vtnihorkulbfejcyzmsqldxpbj",
"vtnghorkulbfmjcyzmsqgdxpaa",
"vtnihorkulbfetcyzmpqudxpaw",
"vtnbhorkulbfejcyzmsqgdupyw",
"ntnihorhulbfejwyzmsqgdxpaw",
"vjnihorkulbfejcyqosqgdxpaw",
"vtiihorbulbfejcbzmsqgdxpaw",
"vtnihorkulbfejxlzmpqgdxpaw",
"vtnihorkolbfejcyfmsqgdxraw",
"vtnihqrrulbfedcyzmsqgdxpaw",
"ctnihorkulbfejcyzmsqgdxpsy",
"vtnihorkulbfkjcezmspgdxpaw",
"ztnihorkulbmcjcyzmsqgdxpaw",
"vinihorkulbfedcyzmsqgdxpau"]));
# Поверителност

<figure markdown>
  ![Поверителност](resources/img/privacy.jpeg){ width="800" }
  <figcaption>Политика за поверителност на <b>Chatrix.One</b></figcaption>
</figure>

## Поверителност на данните

Като оператор на услуга, представляваща алтернатива на наличните методи за интернет комуникация, се стремя към:

- Минимум данни;
- Защитата на на личните данни.

## Неща, които трябва да имате предвид

- **IP** адресите на потребителите **не** се записват по подразбиране. Изключение са случаите, когато се установи опит за неправомерен достъп до системата. При такива ситуации **IP** адресът се записва, за да се предотвратят атаки срещу съответния профил или профили;
- За регистрация **не** се изискват лични данни. Това за съжаление усложнява доказването на собствеността върху профила, в случаите когато паролата трябва да бъде възстановена или променена от администратор.

!!! tip "Съвет"

    Използвайте софтуер за управление на пароли (**Password Manager**). Бих препоръчал [**Bitwarden**](https://bitwarden.com/).

- За да се поддържа синхронизация на съобщенията между няколко устройства и да се обменят съобщения дори когато двама абонати не са онлайн по едно и също време, съобщенията се съхраняват на сървъра за период до 4 седмици. Тази функция се нарича **MAM** (**M**essage **A**rchive **M**anagement) и е активирана по подразбиране, както за индивидуални разговори, така и за **MUC** (**M**ulti **U**ser **C**hats) позната още като **Chatrooms**, за да предложи подобно на комерсиалните месинджъри потребителско изживяване, особено на неопитните потребители на **XMPP**. За собствената си сигурност можете да използвате **OMEMO** (криптиране от край до край), за да запазите разговорите си в безопасност, дори ако системите за защита на моя сървър бъдат компрометирани. Ако не желаете да се съхраняват данни на сървъра вижте раздел [Често Задавани Въпроси](https://docs.chatrix.one/faq/) и по-точно частта [Как да изключа архивирането на съобщенията?](https://docs.chatrix.one/faq/#_28);

- Съдържанието, качено чрез `http_upload` (снимки и други файлове) остава съхранено на сървъра в продължение на 4 седмици;

!!! info "Информация"

    Ако използвате **OMEMO**, снимки и други файлове, не могат да бъдат прочетени. За повече информация вижте [Как би изглеждала снимка, която се съхранява на сървъра в криптиран вид?](https://docs.chatrix.one/faq/#_31).

- Ако съм задължен да сътруднича на органи съгласно приложимото законодателство, информацията ще бъде разкрита в съответствие с приложимото законодателство.

## Преглед на съхраняваните данни

- **IP** адрес на новорегистрирани клиенти - до един час с цел ограничаване броя на регистрациите;
- **IP** адреси на опитите за неправомерен достъп - до шест часа;
- История на съобщенията - четири седмици, но можете да деактивирате от настройките на Вашето приложение (софтуер). За повече информация вижте [Как да изключа архивирането на съобщенията?](https://docs.chatrix.one/faq/#_28);
- Време на последното влизане в системата (за откриване на неактивни потребители);
- Информация за профила и аватар;
- Контакти и **MUC**, добавени към профила;
- Качени файлове - четири седмици.

!!! tip "Съвет"

    Можете да защитите личните си съобщения, като активирате **OMEMO** криптиране от край до край.

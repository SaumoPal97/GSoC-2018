## Documentation
Intially you have to keep all the json files in ```json_dir_1``` directory. Then run the following from command prompt
```
python activity_detector.py
```
You will have list of activities created in the```activity_list.csv``` file. Using all the json files, the ```complete_activity_list.csv``` has been created.
Then run the following
```
python activity_cluster.py
```
This will generate the following clusters of activities generated using the Affinity Propagation algorithm using the Levenshtein distance and 2% of the activities from the shuffled list.
```
 - *Preferences:* CalcTapePreferences, Preferences, PreferencesMain
 - *MainTab:* AnalystTab, EditTask, MainFastF, MainMenu, MainNav, MainTab, SAManual, TabletTab
 - *ForgotPassword:* ForgotPassword
 - *Home:* Home, Howto
 - *BackCountry:* BackCountry
 - *Welcome:* Oblicuos, Welcome
 - *FBReader:* BibleReader, FBReader, NewsReaderHome, Reader
 - *SlidingMenu:* IFunnyMenu, SlidingMenu
 - *ScrollCalendarMain:* ScrollCalendarMain
 - *Browser:* Browser
 - *Browser:* Browser, BrowserApp, MediaBrowser
 - *ProxyAuthDialog:* ProxyAuthDialog
 - *Master:* HafasApp, Markers, Master
 - *GoodsByCategory:* GoodsByCategory, RemediesCategory, VocabularyCategory
 - *Core:* AreaCode, Chord, Core, Course, InfoColorKey, More, t_url
 - *FindMusersOfContacts:* FindMusersOfContacts
 - *TopLevel:* TopLevel
 - *History:* Discovery, History, LoginHistoryUI, Mirror1280, NewsHistory, PinLock, PointsForm
 - *Onboarding:* CBOnboarding, MainOnboardingTou, OnBoarding, OnBoardingFirst, Onboard, Onboarding, OnboardingGroups, OnboardingStep1
 - *AdvSearchContainer:* AdvSearchContainer
 - *HomeScreen:* HomeScreen, InnerScreen, ScreenStream, StarterScreen
 - *Intro:* AppMainIntro, Index, Info, Init, Interview, Intro, InviteFriend, Item, PairIntro, QCIntro
 - *CollegeHockeyNews:* CollegeHockeyNews
 - *SearchCategories:* AllCategories, SearchCategories
 - *Home:* Home
 - *Home:* Boxed, Home
 - *PostInitReplication:* PostInitReplication
 - *SpinningEarth:* MissingData, SpinningEarth, UpcomingEvents
 - *BirthDayHelper:* BirthDayHelper
 - *FieldDefaultsActivty:* FieldDefaultsActivty
 - *train_schedule:* train_schedule
 - *Home:* Home, Hotels
 - *Browser:* Browser
 - *Home:* Games, Home
 - *QuotesShareLoveStickerFragment:* QuotesShareLoveStickerFragment
 - *Home:* Home
 - *Main:* ActMain, CMain, EqMainAdd, FMXNative, Glavna, IAEMain, Main, Main2, Main21, MainUI, Main_, Mainer, MenuSzablon, Mini, OlxMain, Pack, Pasion, PipMain, Quiz, Radio, VingleMain, _Main, _main
 - *InterstitialAd:* Interstitial, InterstitialAd
 - *PinnattaForMessenger:* PinnattaForMessenger
 - *Exercises:* Exercise_, Exercises
 - *ProxyAuthDialog:* ProxyAuthDialog, vPresetDialog
 - *Base:* Aarki, Balance, Base, Pack, PageXP, Pause, PlayCase
 - *WeatherWhiskersMain:* WeatherWhiskersMain
 - *Touts:* Coupons, Documents, Flirts, Groups, RouteStops, Sound, Tests, Text, Tinnitus, TourLite, Touts, Trips, smulk
 - *ScannerRadioTab:* ScannerRadioTab
 - *Chooser:* Chooser
 - *ProxyAuthDialog:* ProxyAuthDialog
 - *PaidSewichiPanel:* PaidSewichiPanel
 - *Notifications:* Notification, NotificationOptions, Notifications
 - *Profile:* Article, Profile, ProfileCreate, ProfileEditor
 - *Resolver:* AmberAlert, BestSeller, MeshClient, Resolver
 - *ProxyAuthDialog:* ProxyAuthDialog
 - *Login:* BrokerLogin, GenericLogin, LeoDict, Lilium, LogIn, LogReg, Login, LoginFacade_, Login_, PreLogin, Songify, UserLogin, _Login
 - *Navigation:* ForumNavigation, Navigation, Navigator, TalkingSpoony
 - *Category:* Categories, Category
 - *Master:* Master, Scanner
 - *Master:* Master, TicketMaster
 - *ProxyAuthDialog:* ProxyAuthDialog
 - *BrowserPreferencesPage:* BrowserPreferencesPage
 - *Camera:* Camera, Chakra, ChargerMap, MemberMain, Parent
 - *Home:* Home
 - *Settings:* Settings, Starting_, SubjectInput
 - *GrantCredentialsWithAcl:* GrantCredentialsWithAcl
 - *Tutorial:* AppTutorial, EditHoliday, MiniTutorial, TruthOrDare, Tutorial, TutorialPages, TutorialSwipe
 - *ProductList:* EasyBlacklist, ProductList, ProductSwipe, Products, ProgramsList
 - *DealSearchResult:* DealSearchResult, HotelSearchResults, PodcastSearchResult, SearchResult
 - *ApplicationSettings:* ApplicationSettings, FloatingIconSettings
 - *Setting:* Series, Setting
 - *Master:* Master
 - *ExpensePaymentMethodList:* ExpensePaymentMethodList
 - *Chooser:* Chooser
 - *Capture:* Capture, CoachMarks, MediaCapture
 - *SeatSelectionScreen:* SeatSelectionScreen
 - *HCDFromCatalogSearchList:* HCDFromCatalogSearchList
 - *OnboardCredentials:* OnboardCredentials
 - *Wizard:* Final_, Primary, SetupWizard, Wizard
 - *Home:* Game, Home
 - *Settings:* Settings
 - *PathfinderOpenReference:* PathfinderOpenReference
 - *Meteo:* Atestamento, Feed, Meteo, Meter, Setup, UpdateLot
 - *ResultadosFutbolMain:* ResultadosFutbolMain
 - *Browser:* Browser
 - *Browser:* Browser, DroidWeb
 - *CircleOfFifths:* CircleOfFifths
 - *Master:* Master
 - *PasswordChange:* FaceMoodScanner, PasswordChange
 - *SplashScreen:* SplashScreen
 - *AdditionalInfo:* AdditionalInfo
 - *Setting:* SelectDevice, Setting
 - *SpotHome:* PhoneHome, SpotHome, TopNavHome, TripItHost, VSPasscode, VisitorHome
 - *AuthorizationClient:* AuthorizationClient
 - *Home:* Episodes, Home
 - *Home:* Home
 - *Master:* Mainer, Master
 - *Registration:* Meditation, RegisterAccount, RegisterDevice, Registration, RegistrationUI, Reservation
 - *Browser:* Browser
 - *MvelopesSlideMenu_:* MvelopesSlideMenu_
 - *LightWeightProxyAuth:* LightWeightProxyAuth
 - *UpgradeCalendar:* UpgradeCalendar, UpgradeStarterKit
 - *AppWall:* AppBrain, AppCoach, AppWall, HandWallet, InAppBilling
 - *UplynkPlayer:* MyMediaPlayer, UnityPlayer, UplynkPlayer
 - *ProductDetail:* ProductActions, ProductDetail, ProductDetails, ProgramDetail
 - *Home:* Home
 - *TermsandConditions:* TermsandConditions
 - *DefaultAirport:* DefaultAirport
 - *Chooser:* Chooser
 - *Time:* BabyTime, Filer, Guide, PTime, Time, Title, Triframe, Type
 - *Home:* Home
 - *GolfSignupProfileAct:* GolfSignupProfileAct
 - *Details:* DCFaqs, Detail, Details, DetailsFree, HotelDetails, QuizDetails, Retail
 - *DevicesList:* DevicesList, MessageList, RecipeList, ServiceHistoryList, TeachersList
 - *KSAFirstUserExperience:* KSAFirstUserExperience
 - *AudioList:* ArticleList, Audio47524, Audio50729, AudioList, ItemsList, QuizList, QuoteList
 - *Welcome:* Welcome
 - *PlayHistories_St2:* PlayHistories_St2
 - *Settings:* Settings
 - *NewMainInterface:* NewMainInterface
 - *Introduction:* Introduction
 - *ItemDetailsScreen:* ItemDetailsScreen
 - *NewsOnePageDetail:* NewsOnePageDetail
 - *RegStepOneLandingPage:* RegStepOneLandingPage
 - *Landing:* Landing, LoginLanding, Tracking
 - *CreateAccount:* CreateAccount, CreateEvent, CreateMealPlan, CreateScoutmark
 - *Home:* Home, HomeYSII
 - *FragmentHolder:* FilterHolder, FragmentHolder, FragmentHost, FragmentManager, FragmentShow, FragmentTV, FragmentWrapper, MainFragmentHolder
 - *ChangeSettings:* CacheSettings, ChangeSettings, LanguageSettings, SnoozeSettings
 - *SlideStack:* AlarmClock, SkillTrack, SlideStack, Slideshow
 - *ManageConnection:* ChooseCollection, CreateConversation, ManageConnection
 - *Dictionary:* Dictionary, DictionaryWords, Questionnaire
 - *TrackBrowser:* PlaylistBrowser, TrackBrowser
 - *MainPage:* AllImages, GuidePages, HangmanGame, Language, MainDingtone, MainLogin, MainMenu, MainPage, Message, MoonPhase, OptionsPage, mainindex
 - *NewTripDestinations:* NewTripDestinations
 - *RBCLChapter:* BookChapters, RBCLChapter, RadioZapper
 - *Authentication:* AudienceNetwork, Authentication, Authenticator, Authorization_, PaymentOptions
 - *SelectFavouritePlayer:* SelectFavouritePlayer
 - *Second:* Second, SingleSound
 - *BaseDrawer:* BaseDrawer, GSGameWrapper, HomeDrawerPhone, ImageRemake, MainDrawer, NewDrawer
 - *ProxyAuthDialog:* ProxyAuthDialog
 - *ChooseLanguageAndExam:* ChooseLanguageAndExam
 - *AndroidLauncher:* AndroidLauncher
 - *HHMilestonesSummary:* HHMilestonesSummary
 - *Master:* Master
 - *MCWelcomeNewUser:* MCWelcomeNewUser
 - *activity_premium_yearly:* activity_premium_yearly
 - *Version:* DialerIcon, Immersive, Termin, VerInfo, VerseEdit, Version, VieraRemote
 - *CBImpression:* CBImpression, DailyExpressions
 - *Post:* Host, Lot, Post, first
 - *NewsDetail:* FoodDetail, HijabDetail, NewDetail, NewsDetail, NewsMain, RegionDetail, SpeciesDetails, WeatherDetail
 - *Home:* ComicHome, Home, HomeMenu
 - *Home:* Home, UserHome
 - *GoogleRssNews:* GoogleRssNews
 - *Browser:* Browser
 - *Home:* Home
 - *BreakiPhone4S:* BreakiPhone4S
 - *Community:* Community, CommunityV2
 - *Master:* Master
 - *State:* Create, Donate, GPSStatus, Shape, Start, Start1, StartGame_, Start_, State, Status, TeamStats
 - *Welcome:* KSAWelcome, WarmWelcome, Welcome
 - *Home:* Home
 - *Settings:* Settings
 - *Weather:* Featured, HealthTest, HelpOthers, Weather, WebFlow, WebviewAd
 - *Chooser:* Chooser
 - *TermsOfUse:* TermsOfUse
 - *Master:* Master
 - *Browser:* Browser, ShowTeam
 - *Chooser:* Chooser
 - *User:* Use, User
 - *Register:* JobFilters, LoginRegister, PageListSearch, Register, RegisterNumber
 - *LanPassTierBenefits_:* LanPassTierBenefits_
 - *Browser:* Browser
 - *Master:* MapFilter, Master
 - *AppList:* AppInvite, AppList, Artists, BookFlight, CouponsList, NewsList, TaskList
 - *MainNavigation:* CategoryNavigation, ChannelNavigator, MainNavigation, ZazzleSideNavigation
 - *BlackAndWhiteBedroomGal4:* BlackAndWhiteBedroomGal4
 - *Home:* Home
 - *MiningStocksAct:* MiningStocksAct
 - *SocialRegisterDialog:* SocialRegisterDialog
 - *AccountConfigure:* AccountConfigure, AccountSignup, NewStudentConfigure
 - *Home:* Home, HomeRd
 - *ProxyAuthDialog:* ProxyAuthDialog
 - *SimpleApp:* DisplayRecipe, MobileNavApp, SimpleApp, SimpleLogin
 - *WelcomeEnrollmentWizard:* WelcomeEnrollmentWizard
 - *Settings:* Settings
 - *Master:* Master
 - *EffectiveWeightLossGuide:* EffectiveWeightLossGuide
 - *Home:* Home
 - *WHTMain:* ActMain, Bjs_Main, GOMusicMain, SubMain, WHTMain
 - *Home:* AHtml, Home
 - *Home:* Home
 - *TelemundoRoot:* TelemundoRoot
 - *Container:* ComicMaker, Container, Coordinates, CountryPicker
 - *Orders:* AddPlayers, AroundMePOIs, Dromoris, Hybrider, Offers, Orders, Prefs, Screen6
 - *WordGuessGame:* WordGuessGame
 - *BackupServiceRegister:* BackupServiceRegister
 - *Dashboard_000:* DashboardNewUi, Dashboard_000
 - *Settings$AppWriteSettings:* Settings$AppWriteSettings
 - *HomePage:* CropImage, FVRHomePage, ForceUpdate, HomeFrame, HomePage, LABsOfferPage
 - *Gallery:* Gallery, Wallpapers_
 - *Home:* Home
 - *ArticleDetail:* ActivitiesMain, ArticleDetail, ArticleDetails, ArticleReader, MagazineDetail, RoutineDetail
 - *VideoPlay:* LessonPlay, VideoGallery, VideoPlay, VideoPlayerNew
 - *Browser:* AlbumBrowser, Browser
 - *Chooser:* Chooser
 - *Master:* Master, Player
 - *Settings:* Settings
 - *Home:* Home
 - *Home:* Home
 - *Search:* AsyncSearch, CarSearch, Earth, Redirect, Schedule, Search, SearchHolder
 - *MonitorYourWeight:* MonitorYourWeight
 - *Splash:* Splash, SplashLogin, TerminalSplash
 - *ShowCoyoteBDCEXP:* ShowCoyoteBDCEXP
 - *AlarmSettings:* AlarmSetting, AlarmSettings, LocatorSettings
 - *Favorites:* FavoriteTeamList, Favorites, Favourites, FranklyVideo
 - *BubblesBrowsing:* BubblesBrowsing
 - *Home:* Home
 - *NavigationDrawer:* NavigationDrawer, NavigationDrawerMain, NavigationPage, NavigationSystem, UINavigationManager
 - *Settings:* Series, Settings
 - *IllusionsProBook:* IllusionsProBook
 - *RegionPicker:* GeoTracker, LocationPicker, NetworkPicker, PhotoPicker, RecipeTabPager, RegionPicker, RingtonePicker
 - *MainScreen:* InitialScreen, LandingScreen, MainScreen, MainSmartphone_, MktScreens, ThornScreen
 - *PublicAccountCard:* PublicAccountCard
 - *Master:* Master
 - *Home:* Help, Home, Hymn, Volume
 - *SleepTimerSettings:* SleepTimeSetup, SleepTimerSettings
 - *BuySellBitcoin:* BuySellBitcoin
 - *Chooser:* Chooser
 - *Home:* Home
 - *SuggestBoardList:* SuggestBoardList
 - *Equalizer:* Equalizer
 - *CurrencyConverter:* CurrencyConverter
 - *ToolsTrainTrack:* ToolsTrainTrack
 - *PhotoInfoMasterFragment:* PhotoInfoMasterFragment
 - *LandingScreenPhone:* LandingScreenPhone
 - *LoggedOutLanding:* LoggedOutLanding
 - *LoginSelection:* CategorySelection, ChannelSelection, ClockSelector, ContactSelection, LanguageSelection, LoginOptions, LoginSelection, VehicleSelected
 - *Lovely:* Live4D, LoseIt, Lovely
 - *FuelDrivingCostSave:* FuelDrivingCostSave
 - *FirstRun:* FirstRun, Hippeastrum2
 - *Master:* Master
 - *Chooser:* ChooseWhip, Chooser
 - *SignUp:* ActSignIn, DontalkSignUp, RingPDP, SignIn, SignUp, Signin, Signup
 - *Overlay:* Overlay, Overview
 - *OnboardCredentials:* OnboardCredentials
 - *Browser:* Browser
 - *Settings$DevelopmentSettings:* Settings$DevelopmentSettings
 - *SolutionTableSettings:* SolutionTableSettings
 - *Home:* Home
 - *Store:* FindStore, GetToken, Share, Store, StoreMenu, Story, Sworkit
 - *Demo:* DICo, Demo, Hello, ItemShop_, Menu, ThemeDemo
 - *Chooser:* Chooser
 - *FullScreen:* BatmobiFullScreenAd, FirstScreen, FullScreen, Fullscreen, FullscreenImage, GalleryFullScreen, PublicArea
 - *Dashboard:* AddDashboardType, DashBoard, Dashboard, Leaderboard
 - *Map:* App, GLMap, InrixMap, MAIN, MM, Map, Maps, Marca, UUB, a
 - *ProxyAuthDialog:* ProxyAuthDialog
 - *About:* About, AboutSystem, Account, LMAuth, Mobiliti
 - *CityList:* CardList, ChatList, CityList, DiaryList, EntryGroupList, NailsList, WishList
 - *CreateOrChooseChat:* CreateOrChooseChat
 - *MainforChattingDUBBED:* MainforChattingDUBBED
 - *Master:* Master, PlusNumber
 - *TermsOfService:* TermsOfService
 - *MainController:* AboutController, MainController, MainTabContainer
 - *Browser:* Browser, CarPower
 - *StreamingFlightResultDetails:* StreamingFlightResultDetails
 - *Master:* Master
 - *Master:* Master
 - *EventDetail:* CasinoDetail, EssayDetail, EventDetail, EventsCitypage, FlightDetails, PaymentDetails
 - *SlackerApp:* SlackerApp
 - *AppInfoArticleList:* AppInfoArticleList
 - *Tab:* Faq, Read, TLTab, Tab, TabMy, TabsApp, Tags, Team, Web
 - *SettingSetBackGround:* SettingSetBackGround
 - *ContentGetBusinessIdeas:* ContentGetBusinessIdeas
 - *Master:* Master
 - *WeatherForecast:* WeatherForecast
 - *LocationCityFragment:* LocationCityFragment
 - *Setting:* Setting
 - *Settings:* Question10, Settings, SettingsV11
 - *Setting:* Setting
 - *Connect:* CarConnect, ColAndCom, Connect, ConnectRatePage, Content, Contingency, ShowComponent
 - *CALesson:* CALesson, NormalLesson
 - *Settings:* SettingPoint, Settings
 - *Setting:* Setting
 - *Submissions:* Permissions, Submissions
 - *EpisodeSearchResultDetail:* EpisodeSearchResultDetail
 - *Description:* Description, OfferDescription
 - *CollectionGallery:* CollectionGallery
 - *Home:* Home
 - *InstalledAppDetails:* InstalledAppDetails
 - *Home:* Glympse, Home
 - *Phrasebook:* Facebook, Phrasebook
 - *PreSignupAssessment:* PreSignupAssessment
 - *Home:* Home
 - *ProxyAuthDialog:* ProxyAuthDialog
 - *ProxyAuthDialog:* ProxyAuthDialog
 - *MainFragment:* MainContentFragment, MainFEjercicios, MainFragment, SCPageFragment
 - *LookupWordScreen:* LookupWordScreen
 - *Master:* Master
 - *Home:* Home
 - *UserSetting:* GeneralSettings, IRCTCSeatMap, UserSetting
 - *NewUserSignUpIntroScreen:* NewUserSignUpIntroScreen
 - *MessagingPreference:* MessagingPreference
 - *Results:* BadResult, LoveQuotes, ResultPage, Results, ResultsAdd, Vegfulek
 - *Home:* Home
 - *FlightTripOverview:* FlightTripOverview
 - *Chooser:* Chooser
 - *SecurityAndPrivacy:* SecurityAndPrivacy
 - *News:* ExpNews, Helps, NewCarHub, NewUser, News, NewsTabbed, Now2, Nurse, Shows, Terms
 - *Location:* Location, LocationSelect, LocationSharing, Locator
 - *Home:* Home, MoPub
 - *UserProfile:* AddEditProfile, AmerenMobile, UserProfile
 - *OffenderRecentAndA2ZActuivity:* OffenderRecentAndA2ZActuivity
 - *MainTopRightDialog:* MainTopRightDialog
 - *WaterMarkTextEditor:* WaterMarkTextEditor
 - *ProxyAuthDialog:* ProxyAuthDialog
 - *Home:* Home
 - *Master:* Master
 - *EditorialVideo:* ESEditorialLanding, EditorialVideo
 - *Settings:* Settings
 - *Home:* Home
 - *Photo:* Chat, Chatroom, CropPhoto, Loto, NewPhoto, Photo, Promo
 - *Ad:* 4, Ad, Andy, Edit, FAQ, Find, H, HH, IM, My, NC, OTP, P, SRP, Sl, Ti, WH, WW, a, er, h, m, ܬ
 - *Master:* Master, MsgThread
 - *GraphingCalculatorProductTour_:* GraphingCalculatorProductTour_
 - *Home:* Home
```
From this list, we can find some prominent activity clusters which will be used to label the training data for the CNNs. The prominent activity clusters are -
 1. SignUp/SignIn/Login/Register
 2. TermsOfUse/TermsOfService/TermsAndConditions
 3. Photo/Video/Camera/Gallery
 4. Ad
 5. Settings
 6. Preferences
 7. Search
 8. Browser
 9. List/Selection/Category/Chooser
 10. OnBoarding/Wizard/Tutorial
 11. Welcome/Landing/Intro
 12. Home/Main/MainTab/HomeScreen
 13. Tab/Menu
 14. Profile/UserProfile
 15. Password/PasswordChange/Authentication
 16. History
 17. Notifications
 18. Reader
 19. Community
 20. Navigation
 21. Time
 22. Weather
 23. Favourites

Now the number of instances for each of them will be calculated using the following python script.
```
python activity_counter.py
```


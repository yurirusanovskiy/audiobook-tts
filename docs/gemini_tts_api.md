Title: Live Content

Description: Fetched live

Source: https://ai.google.dev/gemini-api/docs/speech-generation

---










<!doctype html>
<html 
      lang="en"
      dir="ltr">
  <head>
    <meta name="google-signin-client-id" content="157101835696-ooapojlodmuabs2do2vuhhnf90bccmoi.apps.googleusercontent.com"><meta name="google-signin-scope"
          content="profile email https://www.googleapis.com/auth/developerprofiles https://www.googleapis.com/auth/developerprofiles.award https://www.googleapis.com/auth/devprofiles.full_control.firstparty"><meta property="og:site_name" content="Google AI for Developers">
    <meta property="og:type" content="website"><meta name="theme-color" content="#1967d2"><meta charset="utf-8">
    <meta content="IE=Edge" http-equiv="X-UA-Compatible">
    <meta name="viewport" content="width=device-width, initial-scale=1">
    

    <link rel="manifest" href="/_pwa/googledevai/manifest.json"
          crossorigin="use-credentials">
    <link rel="preconnect" href="//www.gstatic.com" crossorigin>
    <link rel="preconnect" href="//fonts.googleapis.com" crossorigin>
    <link rel="preconnect" href="//www.google-analytics.com" crossorigin><link rel="stylesheet" href="//fonts.googleapis.com/css?family=Google+Sans:400,500|Roboto:400,400italic,500,500italic,700,700italic|Roboto+Mono:400,500,700|Inter:400,500|Inter+Tight:300,500,600&display=swap">
      <link rel="stylesheet"
            href="//fonts.googleapis.com/css2?family=Material+Icons&family=Material+Symbols+Outlined&display=block"><link rel="stylesheet" href="https://www.gstatic.com/devrel-devsite/prod/v5b93ab110c02dc91cc5b79fb160a3c37758bb2dfb04b22b9173ffe5646621934/googledevai/css/app.css">
      
        <link rel="stylesheet" href="https://www.gstatic.com/devrel-devsite/prod/v5b93ab110c02dc91cc5b79fb160a3c37758bb2dfb04b22b9173ffe5646621934/googledevai/css/dark-theme.css" disabled>
      <link rel="shortcut icon" href="https://www.gstatic.com/devrel-devsite/prod/v5b93ab110c02dc91cc5b79fb160a3c37758bb2dfb04b22b9173ffe5646621934/googledevai/images/favicon-new.png">
    <link rel="apple-touch-icon" href="https://www.gstatic.com/devrel-devsite/prod/v5b93ab110c02dc91cc5b79fb160a3c37758bb2dfb04b22b9173ffe5646621934/googledevai/images/touchicon-180-new.png"><link rel="canonical" href="https://ai.google.dev/gemini-api/docs/speech-generation"><link rel="search" type="application/opensearchdescription+xml"
            title="Google AI for Developers" href="https://ai.google.dev/s/opensearch.xml">
      <link rel="alternate" hreflang="en"
          href="https://ai.google.dev/gemini-api/docs/speech-generation" /><link rel="alternate" hreflang="x-default" href="https://ai.google.dev/gemini-api/docs/speech-generation" /><link rel="alternate" hreflang="ar"
          href="https://ai.google.dev/gemini-api/docs/speech-generation?hl=ar" /><link rel="alternate" hreflang="bn"
          href="https://ai.google.dev/gemini-api/docs/speech-generation?hl=bn" /><link rel="alternate" hreflang="zh-Hans"
          href="https://ai.google.dev/gemini-api/docs/speech-generation?hl=zh-cn" /><link rel="alternate" hreflang="zh-Hant"
          href="https://ai.google.dev/gemini-api/docs/speech-generation?hl=zh-tw" /><link rel="alternate" hreflang="fa"
          href="https://ai.google.dev/gemini-api/docs/speech-generation?hl=fa" /><link rel="alternate" hreflang="fr"
          href="https://ai.google.dev/gemini-api/docs/speech-generation?hl=fr" /><link rel="alternate" hreflang="de"
          href="https://ai.google.dev/gemini-api/docs/speech-generation?hl=de" /><link rel="alternate" hreflang="he"
          href="https://ai.google.dev/gemini-api/docs/speech-generation?hl=he" /><link rel="alternate" hreflang="hi"
          href="https://ai.google.dev/gemini-api/docs/speech-generation?hl=hi" /><link rel="alternate" hreflang="id"
          href="https://ai.google.dev/gemini-api/docs/speech-generation?hl=id" /><link rel="alternate" hreflang="it"
          href="https://ai.google.dev/gemini-api/docs/speech-generation?hl=it" /><link rel="alternate" hreflang="ja"
          href="https://ai.google.dev/gemini-api/docs/speech-generation?hl=ja" /><link rel="alternate" hreflang="ko"
          href="https://ai.google.dev/gemini-api/docs/speech-generation?hl=ko" /><link rel="alternate" hreflang="pl"
          href="https://ai.google.dev/gemini-api/docs/speech-generation?hl=pl" /><link rel="alternate" hreflang="pt-BR"
          href="https://ai.google.dev/gemini-api/docs/speech-generation?hl=pt-br" /><link rel="alternate" hreflang="ru"
          href="https://ai.google.dev/gemini-api/docs/speech-generation?hl=ru" /><link rel="alternate" hreflang="es-419"
          href="https://ai.google.dev/gemini-api/docs/speech-generation?hl=es-419" /><link rel="alternate" hreflang="th"
          href="https://ai.google.dev/gemini-api/docs/speech-generation?hl=th" /><link rel="alternate" hreflang="tr"
          href="https://ai.google.dev/gemini-api/docs/speech-generation?hl=tr" /><link rel="alternate" hreflang="vi"
          href="https://ai.google.dev/gemini-api/docs/speech-generation?hl=vi" /><link rel="alternate" hreflang="sq"
          href="https://ai.google.dev/gemini-api/docs/speech-generation?hl=sq" /><title>Gemini API &nbsp;|&nbsp; Google AI for Developers</title>

<meta property="og:title" content="Gemini API &nbsp;|&nbsp; Google AI for Developers"><meta name="description" content="Get started generating audio with the Gemini API">
  <meta property="og:description" content="Get started generating audio with the Gemini API"><meta property="og:url" content="https://ai.google.dev/gemini-api/docs/speech-generation"><meta property="og:image" content="https://ai.google.dev/static/site-assets/images/share-gemini-api-2.png">
  <meta property="og:image:width" content="1200">
  <meta property="og:image:height" content="675"><meta property="og:locale" content="en"><meta name="twitter:card" content="summary_large_image"><script type="application/ld+json">
  {
    "@context": "https://schema.org",
    "@type": "Article",
    
    "headline": ""
  }
</script>
  

  

  

  

  


    </head>
  <body class="gemini-api color-scheme--light"
        template="page"
        theme="googledevai-theme"
        type="article"
        
        appearance
        
        layout="docs"
        
        
        
        
        
        display-toc
        pending>
  
    <devsite-progress type="indeterminate" id="app-progress"></devsite-progress>
  
  
    <a href="#main-content" class="skip-link button">
      
      Skip to main content
    </a>
    <section class="devsite-wrapper">
      <devsite-cookie-notification-bar></devsite-cookie-notification-bar>
        <devsite-header role="banner" keep-tabs-visible>
  
    





















<div class="devsite-header--inner" data-nosnippet>
  <div class="devsite-top-logo-row-wrapper-wrapper">
    <div class="devsite-top-logo-row-wrapper">
      <div class="devsite-top-logo-row">
        <button type="button" id="devsite-hamburger-menu"
          class="devsite-header-icon-button button-flat material-icons gc-analytics-event"
          data-category="Site-Wide Custom Events"
          data-label="Navigation menu button"
          visually-hidden
          aria-label="Open menu">
        </button>
        
<div class="devsite-product-name-wrapper">

  <a href="/" class="devsite-site-logo-link gc-analytics-event"
   data-category="Site-Wide Custom Events" data-label="Site logo" track-type="globalNav"
   track-name="geminiAPI" track-metadata-position="nav"
   track-metadata-eventDetail="nav">
  
  <picture>
    
    <source srcset="https://ai.google.dev/_static/googledevai/images/gemini-api-logo-dark-theme.svg"
            media="(prefers-color-scheme: dark)"
            class="devsite-dark-theme">
    
    <img src="https://ai.google.dev/_static/googledevai/images/gemini-api-logo.svg" class="devsite-site-logo" alt="Gemini API">
  </picture>
  
</a>



  
  
  <span class="devsite-product-name">
    <ul class="devsite-breadcrumb-list"
  >
  
  <li class="devsite-breadcrumb-item
             ">
    
    
    
      
      
    
  </li>
  
</ul>
  </span>

</div>
        <div class="devsite-top-logo-row-middle">
          <div class="devsite-header-upper-tabs">
            
           </div>
          
<devsite-search
    enable-signin
    enable-search
    enable-suggestions
      enable-query-completion
    
    enable-search-summaries
    project-name="Gemini API"
    tenant-name="Google AI for Developers"
    project-scope="/gemini-api/docs/generate-content"
    url-scoped="https://ai.google.dev/s/results/gemini-api/docs/generate-content"
    
    
    
    >
  <form class="devsite-search-form" action="https://ai.google.dev/s/results" method="GET">
    <div class="devsite-search-container">
      <button type="button"
              search-open
              class="devsite-search-button devsite-header-icon-button button-flat material-icons"
              
              aria-label="Open search"></button>
      <div class="devsite-searchbox">
        <input
          aria-activedescendant=""
          aria-autocomplete="list"
          
          aria-label="Search"
          aria-expanded="false"
          aria-haspopup="listbox"
          autocomplete="off"
          class="devsite-search-field devsite-search-query"
          name="q"
          
          placeholder="Search"
          role="combobox"
          type="text"
          value=""
          >
          <div class="devsite-search-image material-icons" aria-hidden="true">
            
              <svg class="devsite-search-ai-image" width="24" height="24" viewBox="0 0 24 24" fill="none" xmlns="http://www.w3.org/2000/svg">
                  <g clip-path="url(#clip0_6641_386)">
                    <path d="M19.6 21L13.3 14.7C12.8 15.1 12.225 15.4167 11.575 15.65C10.925 15.8833 10.2333 16 9.5 16C7.68333 16 6.14167 15.375 4.875 14.125C3.625 12.8583 3 11.3167 3 9.5C3 7.68333 3.625 6.15 4.875 4.9C6.14167 3.63333 7.68333 3 9.5 3C10.0167 3 10.5167 3.05833 11 3.175C11.4833 3.275 11.9417 3.43333 12.375 3.65L10.825 5.2C10.6083 5.13333 10.3917 5.08333 10.175 5.05C9.95833 5.01667 9.73333 5 9.5 5C8.25 5 7.18333 5.44167 6.3 6.325C5.43333 7.19167 5 8.25 5 9.5C5 10.75 5.43333 11.8167 6.3 12.7C7.18333 13.5667 8.25 14 9.5 14C10.6667 14 11.6667 13.625 12.5 12.875C13.35 12.1083 13.8417 11.15 13.975 10H15.975C15.925 10.6333 15.7833 11.2333 15.55 11.8C15.3333 12.3667 15.05 12.8667 14.7 13.3L21 19.6L19.6 21ZM17.5 12C17.5 10.4667 16.9667 9.16667 15.9 8.1C14.8333 7.03333 13.5333 6.5 12 6.5C13.5333 6.5 14.8333 5.96667 15.9 4.9C16.9667 3.83333 17.5 2.53333 17.5 0.999999C17.5 2.53333 18.0333 3.83333 19.1 4.9C20.1667 5.96667 21.4667 6.5 23 6.5C21.4667 6.5 20.1667 7.03333 19.1 8.1C18.0333 9.16667 17.5 10.4667 17.5 12Z" fill="#5F6368"/>
                  </g>
                <defs>
                <clipPath id="clip0_6641_386">
                <rect width="24" height="24" fill="white"/>
                </clipPath>
                </defs>
              </svg>
            
          </div>
          <div class="devsite-search-shortcut-icon-container" aria-hidden="true">
            <kbd class="devsite-search-shortcut-icon">/</kbd>
          </div>
      </div>
    </div>
  </form>
  <button type="button"
          search-close
          class="devsite-search-button devsite-header-icon-button button-flat material-icons"
          
          aria-label="Close search"></button>
</devsite-search>

        </div>

        

          

          

          

          <devsite-appearance-selector></devsite-appearance-selector>

          
<devsite-language-selector>
  <ul role="presentation">
    
    
    <li role="presentation">
      <a role="menuitem" lang="en"
        >English</a>
    </li>
    
    <li role="presentation">
      <a role="menuitem" lang="de"
        >Deutsch</a>
    </li>
    
    <li role="presentation">
      <a role="menuitem" lang="es_419"
        >Español – América Latina</a>
    </li>
    
    <li role="presentation">
      <a role="menuitem" lang="fr"
        >Français</a>
    </li>
    
    <li role="presentation">
      <a role="menuitem" lang="id"
        >Indonesia</a>
    </li>
    
    <li role="presentation">
      <a role="menuitem" lang="it"
        >Italiano</a>
    </li>
    
    <li role="presentation">
      <a role="menuitem" lang="pl"
        >Polski</a>
    </li>
    
    <li role="presentation">
      <a role="menuitem" lang="pt_br"
        >Português – Brasil</a>
    </li>
    
    <li role="presentation">
      <a role="menuitem" lang="sq"
        >Shqip</a>
    </li>
    
    <li role="presentation">
      <a role="menuitem" lang="vi"
        >Tiếng Việt</a>
    </li>
    
    <li role="presentation">
      <a role="menuitem" lang="tr"
        >Türkçe</a>
    </li>
    
    <li role="presentation">
      <a role="menuitem" lang="ru"
        >Русский</a>
    </li>
    
    <li role="presentation">
      <a role="menuitem" lang="he"
        >עברית</a>
    </li>
    
    <li role="presentation">
      <a role="menuitem" lang="ar"
        >العربيّة</a>
    </li>
    
    <li role="presentation">
      <a role="menuitem" lang="fa"
        >فارسی</a>
    </li>
    
    <li role="presentation">
      <a role="menuitem" lang="hi"
        >हिंदी</a>
    </li>
    
    <li role="presentation">
      <a role="menuitem" lang="bn"
        >বাংলা</a>
    </li>
    
    <li role="presentation">
      <a role="menuitem" lang="th"
        >ภาษาไทย</a>
    </li>
    
    <li role="presentation">
      <a role="menuitem" lang="zh_cn"
        >中文 – 简体</a>
    </li>
    
    <li role="presentation">
      <a role="menuitem" lang="zh_tw"
        >中文 – 繁體</a>
    </li>
    
    <li role="presentation">
      <a role="menuitem" lang="ja"
        >日本語</a>
    </li>
    
    <li role="presentation">
      <a role="menuitem" lang="ko"
        >한국어</a>
    </li>
    
  </ul>
</devsite-language-selector>


          
            <a class="devsite-header-link devsite-top-button button gc-analytics-event "
    href="https://aistudio.google.com/apikey"
    data-category="Site-Wide Custom Events"
    data-label="Site header link: Get API key"
    
      
        target="_blank"
      
    >
  Get API key
</a>
          
            <a class="devsite-header-link devsite-top-button button gc-analytics-event "
    href="https://github.com/google-gemini/cookbook"
    data-category="Site-Wide Custom Events"
    data-label="Site header link: Cookbook"
    
      
        target="_blank"
      
    >
  Cookbook
</a>
          
            <a class="devsite-header-link devsite-top-button button gc-analytics-event "
    href="https://discuss.ai.google.dev/c/gemini-api/"
    data-category="Site-Wide Custom Events"
    data-label="Site header link: Community"
    
      
        target="_blank"
      
    >
  Community
</a>
          

        

        
          <devsite-user 
                        
                        
                          enable-profiles
                        
                        
                        id="devsite-user">
            
              
              <span class="button devsite-top-button" aria-hidden="true" visually-hidden>Sign in</span>
            
          </devsite-user>
        
        
        
      </div>
    </div>
  </div>



  <div class="devsite-collapsible-section
    ">
    <div class="devsite-header-background">
      
        
      
      
        <div class="devsite-doc-set-nav-row">
          
          
            
            
  <devsite-tabs class="lower-tabs">

    <nav class="devsite-tabs-wrapper" aria-label="Lower tabs">
      
        
          <tab  class="devsite-active">
            
    <a href="https://ai.google.dev/gemini-api/docs"
    class="devsite-tabs-content gc-analytics-event "
      track-metadata-eventdetail="https://ai.google.dev/gemini-api/docs"
    
       track-type="nav"
       track-metadata-position="nav - docs"
       track-metadata-module="primary nav"
       aria-label="Docs, selected" 
       
         
           data-category="Site-Wide Custom Events"
         
           data-label="Tab: Docs"
         
           track-name="docs"
         
       >
    Docs
  
    </a>
    
  
          </tab>
        
      
        
          <tab  >
            
    <a href="https://ai.google.dev/api"
    class="devsite-tabs-content gc-analytics-event "
      track-metadata-eventdetail="https://ai.google.dev/api"
    
       track-type="nav"
       track-metadata-position="nav - api reference"
       track-metadata-module="primary nav"
       
       
         
           data-category="Site-Wide Custom Events"
         
           data-label="Tab: API reference"
         
           track-name="api reference"
         
       >
    API reference
  
    </a>
    
  
          </tab>
        
      
    </nav>

  </devsite-tabs>

          
          
        </div>
      
    </div>
  </div>

</div>



  

  
</devsite-header>
        <devsite-book-nav scrollbars >
          
            





















<div class="devsite-book-nav-filter"
     hidden>
  <span class="filter-list-icon material-icons" aria-hidden="true"></span>
  <input type="text"
         placeholder="Filter"
         
         aria-label="Type to filter"
         role="searchbox">
  
  <span class="filter-clear-button hidden"
        data-title="Clear filter"
        aria-label="Clear filter"
        role="button"
        tabindex="0"></span>
</div>

<nav class="devsite-book-nav devsite-nav nocontent" data-nosnippet
     aria-label="Side menu">
  <div class="devsite-mobile-header">
    <button type="button"
            id="devsite-close-nav"
            class="devsite-header-icon-button button-flat material-icons gc-analytics-event"
            data-category="Site-Wide Custom Events"
            data-label="Close navigation"
            aria-label="Close navigation">
    </button>
    <div class="devsite-product-name-wrapper">

  <a href="/" class="devsite-site-logo-link gc-analytics-event"
   data-category="Site-Wide Custom Events" data-label="Site logo" track-type="globalNav"
   track-name="geminiAPI" track-metadata-position="nav"
   track-metadata-eventDetail="nav">
  
  <picture>
    
    <source srcset="https://ai.google.dev/_static/googledevai/images/gemini-api-logo-dark-theme.svg"
            media="(prefers-color-scheme: dark)"
            class="devsite-dark-theme">
    
    <img src="https://ai.google.dev/_static/googledevai/images/gemini-api-logo.svg" class="devsite-site-logo" alt="Gemini API">
  </picture>
  
</a>


  
      <span class="devsite-product-name">
        
        
        <ul class="devsite-breadcrumb-list"
  >
  
  <li class="devsite-breadcrumb-item
             ">
    
    
    
      
      
    
  </li>
  
</ul>
      </span>
    

</div>
  </div>

  <div class="devsite-book-nav-wrapper">
    <div class="devsite-mobile-nav-top">
      
        <ul class="devsite-nav-list">
          
            <li class="devsite-nav-item">
              
  
  <a href="/gemini-api/docs"
    
       class="devsite-nav-title gc-analytics-event
              
              devsite-nav-active"
    

    
      
        data-category="Site-Wide Custom Events"
      
        data-label="Tab: Gemini API"
      
        track-name="gemini api"
      
    
     data-category="Site-Wide Custom Events"
     data-label="Responsive Tab: Gemini API"
     track-type="globalNav"
     track-metadata-eventDetail="globalMenu"
     track-metadata-position="nav">
  
    <span class="devsite-nav-text" tooltip >
      Gemini API
   </span>
    
  
  </a>
  

  
              
                <ul class="devsite-nav-responsive-tabs">
                  
                    
                    
                    
                    <li class="devsite-nav-item">
                      
  
  <a href="/gemini-api/docs"
    
       class="devsite-nav-title gc-analytics-event
              
              devsite-nav-active"
    

    
      
        data-category="Site-Wide Custom Events"
      
        data-label="Tab: Docs"
      
        track-name="docs"
      
    
     data-category="Site-Wide Custom Events"
     data-label="Responsive Tab: Docs"
     track-type="globalNav"
     track-metadata-eventDetail="globalMenu"
     track-metadata-position="nav">
  
    <span class="devsite-nav-text" tooltip menu="_book">
      Docs
   </span>
    
  
  </a>
  

  
                    </li>
                  
                    
                    
                    
                    <li class="devsite-nav-item">
                      
  
  <a href="/api"
    
       class="devsite-nav-title gc-analytics-event
              
              "
    

    
      
        data-category="Site-Wide Custom Events"
      
        data-label="Tab: API reference"
      
        track-name="api reference"
      
    
     data-category="Site-Wide Custom Events"
     data-label="Responsive Tab: API reference"
     track-type="globalNav"
     track-metadata-eventDetail="globalMenu"
     track-metadata-position="nav">
  
    <span class="devsite-nav-text" tooltip >
      API reference
   </span>
    
  
  </a>
  

  
                    </li>
                  
                </ul>
              
            </li>
          
          
    
    
<li class="devsite-nav-item">

  
  <a href="https://aistudio.google.com/apikey"
    
       class="devsite-nav-title gc-analytics-event "
    

    
      
        target="_blank"
      
    
     data-category="Site-Wide Custom Events"
     data-label="Responsive Tab: Get API key"
     track-type="navMenu"
     track-metadata-eventDetail="globalMenu"
     track-metadata-position="nav">
  
    <span class="devsite-nav-text" tooltip >
      Get API key
   </span>
    
  
  </a>
  

</li>

  
    
    
<li class="devsite-nav-item">

  
  <a href="https://github.com/google-gemini/cookbook"
    
       class="devsite-nav-title gc-analytics-event "
    

    
      
        target="_blank"
      
    
     data-category="Site-Wide Custom Events"
     data-label="Responsive Tab: Cookbook"
     track-type="navMenu"
     track-metadata-eventDetail="globalMenu"
     track-metadata-position="nav">
  
    <span class="devsite-nav-text" tooltip >
      Cookbook
   </span>
    
  
  </a>
  

</li>

  
    
    
<li class="devsite-nav-item">

  
  <a href="https://discuss.ai.google.dev/c/gemini-api/"
    
       class="devsite-nav-title gc-analytics-event "
    

    
      
        target="_blank"
      
    
     data-category="Site-Wide Custom Events"
     data-label="Responsive Tab: Community"
     track-type="navMenu"
     track-metadata-eventDetail="globalMenu"
     track-metadata-position="nav">
  
    <span class="devsite-nav-text" tooltip >
      Community
   </span>
    
  
  </a>
  

</li>

  
          
        </ul>
      
    </div>
    
      <div class="devsite-mobile-nav-bottom">
        
          
          <ul class="devsite-nav-list" menu="_book">
            <li class="devsite-nav-item
           devsite-nav-heading"><div class="devsite-nav-title devsite-nav-title-no-path">
        <span class="devsite-nav-text" tooltip>Get started</span>
      </div></li>

  <li class="devsite-nav-item"><a href="/gemini-api/docs"
        class="devsite-nav-title"
      ><span class="devsite-nav-text" tooltip>Overview</span></a></li>

  <li class="devsite-nav-item"><a href="/gemini-api/docs/quickstart"
        class="devsite-nav-title"
      ><span class="devsite-nav-text" tooltip>Quickstart</span></a></li>

  <li class="devsite-nav-item"><a href="/gemini-api/docs/api-key"
        class="devsite-nav-title"
      ><span class="devsite-nav-text" tooltip>API keys</span></a></li>

  <li class="devsite-nav-item"><a href="/gemini-api/docs/libraries"
        class="devsite-nav-title"
      ><span class="devsite-nav-text" tooltip>Libraries</span></a></li>

  <li class="devsite-nav-item"><a href="/gemini-api/docs/pricing"
        class="devsite-nav-title"
      ><span class="devsite-nav-text" tooltip>Pricing</span></a></li>

  <li class="devsite-nav-item
           devsite-nav-beta"><a href="/gemini-api/docs/interactions-overview"
        class="devsite-nav-title"
      ><span class="devsite-nav-text" tooltip>Interactions API</span><span class="devsite-nav-icon material-icons"
        data-icon="beta"
        data-title="Beta"
        aria-hidden="true"></span></a></li>

  <li class="devsite-nav-item"><a href="/gemini-api/docs/coding-agents"
        class="devsite-nav-title"
      ><span class="devsite-nav-text" tooltip>Coding agent setup</span></a></li>

  <li class="devsite-nav-item
           devsite-nav-heading"><div class="devsite-nav-title devsite-nav-title-no-path">
        <span class="devsite-nav-text" tooltip>Models</span>
      </div></li>

  <li class="devsite-nav-item"><a href="/gemini-api/docs/models"
        class="devsite-nav-title"
      
        alt-paths=" /gemini-api/docs/models/gemini-3.1-flash-image /gemini-api/docs/models/gemini-3.1-pro-preview /gemini-api/docs/models/gemini-3-pro-preview /gemini-api/docs/models/gemini-3-pro-image /gemini-api/docs/models/gemini-3.5-flash /gemini-api/docs/models/gemini-3-flash-preview /gemini-api/docs/models/gemini-3.1-flash-tts-preview /gemini-api/docs/models/veo-3.1-lite-generate-preview /gemini-api/docs/models/gemini-3.1-flash-live-preview /gemini-api/docs/models/gemini-3.1-flash-lite /gemini-api/docs/models/gemini-3.1-flash-lite-preview /gemini-api/docs/models/gemini-2.5-flash /gemini-api/docs/models/gemini-2.5-flash-preview-09-2025 /gemini-api/docs/models/gemini-2.5-flash-image /gemini-api/docs/models/gemini-2.5-flash-native-audio-preview-12-2025 /gemini-api/docs/models/gemini-2.5-flash-preview-tts /gemini-api/docs/models/gemini-2.5-flash-lite /gemini-api/docs/models/gemini-2.5-flash-lite-preview-09-2025 /gemini-api/docs/models/gemini-2.5-pro /gemini-api/docs/models/gemini-2.5-pro-preview-tts /gemini-api/docs/models/gemini-2.0-flash /gemini-api/docs/models/gemini-2.0-flash-lite /gemini-api/docs/models/imagen /gemini-api/docs/models/veo-3.1-generate-preview /gemini-api/docs/models/veo-2.0-generate-001 /gemini-api/docs/models/gemini-embedding-001 /gemini-api/docs/models/gemini-embedding-2 /gemini-api/docs/models/gemini-robotics-er-1.5-preview /gemini-api/docs/models/gemini-robotics-er-1.6-preview /gemini-api/docs/models/deep-research-pro-preview-12-2025 /gemini-api/docs/models/deep-research-preview-04-2026 /gemini-api/docs/models/deep-research-max-preview-04-2026 /gemini-api/docs/models/antigravity-preview-05-2026 /gemini-api/docs/models/lyria-realtime-exp /gemini-api/docs/models/lyria-3-clip-preview /gemini-api/docs/models/lyria-3-pro-preview "><span class="devsite-nav-text" tooltip>All models</span></a></li>

  <li class="devsite-nav-item"><a href="/gemini-api/docs/whats-new-gemini-3.5"
        class="devsite-nav-title"
      ><span class="devsite-nav-text" tooltip>Current: Gemini 3.5</span></a></li>

  <li class="devsite-nav-item"><a href="/gemini-api/docs/image-generation"
        class="devsite-nav-title"
      ><span class="devsite-nav-text" tooltip>Nano Banana</span></a></li>

  <li class="devsite-nav-item"><a href="/gemini-api/docs/video"
        class="devsite-nav-title"
      ><span class="devsite-nav-text" tooltip>Veo</span></a></li>

  <li class="devsite-nav-item
           devsite-nav-preview"><a href="/gemini-api/docs/music-generation"
        class="devsite-nav-title"
      ><span class="devsite-nav-text" tooltip>Lyria 3</span><span class="devsite-nav-icon material-icons"
        data-icon="preview"
        data-title="Preview"
        aria-hidden="true"></span></a></li>

  <li class="devsite-nav-item"><a href="/gemini-api/docs/realtime-music-generation"
        class="devsite-nav-title"
      ><span class="devsite-nav-text" tooltip>Lyria RealTime</span></a></li>

  <li class="devsite-nav-item"><a href="/gemini-api/docs/imagen"
        class="devsite-nav-title"
      ><span class="devsite-nav-text" tooltip>Imagen</span></a></li>

  <li class="devsite-nav-item"><a href="/gemini-api/docs/speech-generation"
        class="devsite-nav-title"
      ><span class="devsite-nav-text" tooltip>Text-to-speech</span></a></li>

  <li class="devsite-nav-item"><a href="/gemini-api/docs/embeddings"
        class="devsite-nav-title"
      ><span class="devsite-nav-text" tooltip>Embeddings</span></a></li>

  <li class="devsite-nav-item
           devsite-nav-preview"><a href="/gemini-api/docs/robotics-overview"
        class="devsite-nav-title"
      ><span class="devsite-nav-text" tooltip>Robotics</span><span class="devsite-nav-icon material-icons"
        data-icon="preview"
        data-title="Preview"
        aria-hidden="true"></span></a></li>

  <li class="devsite-nav-item
           devsite-nav-heading"><div class="devsite-nav-title devsite-nav-title-no-path">
        <span class="devsite-nav-text" tooltip>Core capabilities</span>
      </div></li>

  <li class="devsite-nav-item"><a href="/gemini-api/docs/text-generation"
        class="devsite-nav-title"
      ><span class="devsite-nav-text" tooltip>Text</span></a></li>

  <li class="devsite-nav-item
           devsite-nav-expandable"><div class="devsite-expandable-nav">
      <a class="devsite-nav-toggle" aria-hidden="true"></a><div class="devsite-nav-title devsite-nav-title-no-path" tabindex="0" role="button">
        <span class="devsite-nav-text" tooltip>Image</span>
      </div><ul class="devsite-nav-section"><li class="devsite-nav-item"><a href="/gemini-api/docs/image-generation"
        class="devsite-nav-title"
      ><span class="devsite-nav-text" tooltip>Image generation 🍌</span></a></li><li class="devsite-nav-item"><a href="/gemini-api/docs/image-understanding"
        class="devsite-nav-title"
      ><span class="devsite-nav-text" tooltip>Image understanding</span></a></li></ul></div></li>

  <li class="devsite-nav-item
           devsite-nav-expandable"><div class="devsite-expandable-nav">
      <a class="devsite-nav-toggle" aria-hidden="true"></a><div class="devsite-nav-title devsite-nav-title-no-path" tabindex="0" role="button">
        <span class="devsite-nav-text" tooltip>Video</span>
      </div><ul class="devsite-nav-section"><li class="devsite-nav-item"><a href="/gemini-api/docs/video"
        class="devsite-nav-title"
      ><span class="devsite-nav-text" tooltip>Video generation</span></a></li><li class="devsite-nav-item"><a href="/gemini-api/docs/video-understanding"
        class="devsite-nav-title"
      ><span class="devsite-nav-text" tooltip>Video understanding</span></a></li></ul></div></li>

  <li class="devsite-nav-item"><a href="/gemini-api/docs/document-processing"
        class="devsite-nav-title"
      ><span class="devsite-nav-text" tooltip>Documents</span></a></li>

  <li class="devsite-nav-item
           devsite-nav-expandable"><div class="devsite-expandable-nav">
      <a class="devsite-nav-toggle" aria-hidden="true"></a><div class="devsite-nav-title devsite-nav-title-no-path" tabindex="0" role="button">
        <span class="devsite-nav-text" tooltip>Speech and audio</span>
      </div><ul class="devsite-nav-section"><li class="devsite-nav-item
           devsite-nav-preview"><a href="/gemini-api/docs/speech-generation"
        class="devsite-nav-title"
      ><span class="devsite-nav-text" tooltip>Speech generation</span><span class="devsite-nav-icon material-icons"
        data-icon="preview"
        data-title="Preview"
        aria-hidden="true"></span></a></li><li class="devsite-nav-item"><a href="/gemini-api/docs/audio"
        class="devsite-nav-title"
      ><span class="devsite-nav-text" tooltip>Audio understanding</span></a></li></ul></div></li>

  <li class="devsite-nav-item
           devsite-nav-expandable"><div class="devsite-expandable-nav">
      <a class="devsite-nav-toggle" aria-hidden="true"></a><div class="devsite-nav-title devsite-nav-title-no-path" tabindex="0" role="button">
        <span class="devsite-nav-text" tooltip>Thinking</span>
      </div><ul class="devsite-nav-section"><li class="devsite-nav-item"><a href="/gemini-api/docs/thinking"
        class="devsite-nav-title"
      ><span class="devsite-nav-text" tooltip>Thinking</span></a></li><li class="devsite-nav-item"><a href="/gemini-api/docs/thought-signatures"
        class="devsite-nav-title"
      ><span class="devsite-nav-text" tooltip>Thought signatures</span></a></li></ul></div></li>

  <li class="devsite-nav-item"><a href="/gemini-api/docs/structured-output"
        class="devsite-nav-title"
      ><span class="devsite-nav-text" tooltip>Structured outputs</span></a></li>

  <li class="devsite-nav-item"><a href="/gemini-api/docs/function-calling"
        class="devsite-nav-title"
      ><span class="devsite-nav-text" tooltip>Function calling</span></a></li>

  <li class="devsite-nav-item"><a href="/gemini-api/docs/long-context"
        class="devsite-nav-title"
      ><span class="devsite-nav-text" tooltip>Long context</span></a></li>

  <li class="devsite-nav-item
           devsite-nav-heading"><div class="devsite-nav-title devsite-nav-title-no-path">
        <span class="devsite-nav-text" tooltip>Agents</span>
      </div></li>

  <li class="devsite-nav-item"><a href="/gemini-api/docs/agents"
        class="devsite-nav-title"
      ><span class="devsite-nav-text" tooltip>Overview</span></a></li>

  <li class="devsite-nav-item"><a href="/gemini-api/docs/managed-agents-quickstart"
        class="devsite-nav-title"
      ><span class="devsite-nav-text" tooltip>Quickstart</span></a></li>

  <li class="devsite-nav-item
           devsite-nav-preview"><a href="/gemini-api/docs/antigravity-agent"
        class="devsite-nav-title"
      ><span class="devsite-nav-text" tooltip>Antigravity Agent</span><span class="devsite-nav-icon material-icons"
        data-icon="preview"
        data-title="Preview"
        aria-hidden="true"></span></a></li>

  <li class="devsite-nav-item"><a href="/gemini-api/docs/custom-agents"
        class="devsite-nav-title"
      ><span class="devsite-nav-text" tooltip>Building managed agents</span></a></li>

  <li class="devsite-nav-item"><a href="/gemini-api/docs/agent-environment"
        class="devsite-nav-title"
      ><span class="devsite-nav-text" tooltip>Environments</span></a></li>

  <li class="devsite-nav-item
           devsite-nav-preview"><a href="/gemini-api/docs/interactions/deep-research"
        class="devsite-nav-title"
      ><span class="devsite-nav-text" tooltip>Deep Research Agent</span><span class="devsite-nav-icon material-icons"
        data-icon="preview"
        data-title="Preview"
        aria-hidden="true"></span></a></li>

  <li class="devsite-nav-item
           devsite-nav-heading"><div class="devsite-nav-title devsite-nav-title-no-path">
        <span class="devsite-nav-text" tooltip>Tools</span>
      </div></li>

  <li class="devsite-nav-item"><a href="/gemini-api/docs/tools"
        class="devsite-nav-title"
      ><span class="devsite-nav-text" tooltip>Overview</span></a></li>

  <li class="devsite-nav-item"><a href="/gemini-api/docs/google-search"
        class="devsite-nav-title"
      ><span class="devsite-nav-text" tooltip>Google Search</span></a></li>

  <li class="devsite-nav-item"><a href="/gemini-api/docs/maps-grounding"
        class="devsite-nav-title"
      ><span class="devsite-nav-text" tooltip>Google Maps</span></a></li>

  <li class="devsite-nav-item"><a href="/gemini-api/docs/code-execution"
        class="devsite-nav-title"
      ><span class="devsite-nav-text" tooltip>Code execution</span></a></li>

  <li class="devsite-nav-item"><a href="/gemini-api/docs/url-context"
        class="devsite-nav-title"
      ><span class="devsite-nav-text" tooltip>URL context</span></a></li>

  <li class="devsite-nav-item
           devsite-nav-preview"><a href="/gemini-api/docs/computer-use"
        class="devsite-nav-title"
      ><span class="devsite-nav-text" tooltip>Computer Use</span><span class="devsite-nav-icon material-icons"
        data-icon="preview"
        data-title="Preview"
        aria-hidden="true"></span></a></li>

  <li class="devsite-nav-item"><a href="/gemini-api/docs/file-search"
        class="devsite-nav-title"
      ><span class="devsite-nav-text" tooltip>File Search</span></a></li>

  <li class="devsite-nav-item
           devsite-nav-preview"><a href="/gemini-api/docs/tool-combination"
        class="devsite-nav-title"
      ><span class="devsite-nav-text" tooltip>Combine Tools and Function calling</span><span class="devsite-nav-icon material-icons"
        data-icon="preview"
        data-title="Preview"
        aria-hidden="true"></span></a></li>

  <li class="devsite-nav-item
           devsite-nav-heading"><div class="devsite-nav-title devsite-nav-title-no-path">
        <span class="devsite-nav-text" tooltip>Live API</span>
      </div></li>

  <li class="devsite-nav-item"><a href="/gemini-api/docs/live-api"
        class="devsite-nav-title"
      ><span class="devsite-nav-text" tooltip>Overview</span></a></li>

  <li class="devsite-nav-item
           devsite-nav-expandable"><div class="devsite-expandable-nav">
      <a class="devsite-nav-toggle" aria-hidden="true"></a><div class="devsite-nav-title devsite-nav-title-no-path" tabindex="0" role="button">
        <span class="devsite-nav-text" tooltip>Get started</span>
      </div><ul class="devsite-nav-section"><li class="devsite-nav-item"><a href="/gemini-api/docs/live-api/get-started-sdk"
        class="devsite-nav-title"
      ><span class="devsite-nav-text" tooltip>Get started using the GenAI SDK</span></a></li><li class="devsite-nav-item"><a href="/gemini-api/docs/live-api/get-started-websocket"
        class="devsite-nav-title"
      ><span class="devsite-nav-text" tooltip>Get started using raw WebSockets</span></a></li></ul></div></li>

  <li class="devsite-nav-item"><a href="/gemini-api/docs/live-api/capabilities"
        class="devsite-nav-title"
      ><span class="devsite-nav-text" tooltip>Capabilities</span></a></li>

  <li class="devsite-nav-item"><a href="/gemini-api/docs/live-api/tools"
        class="devsite-nav-title"
      ><span class="devsite-nav-text" tooltip>Tool use</span></a></li>

  <li class="devsite-nav-item"><a href="/gemini-api/docs/live-api/session-management"
        class="devsite-nav-title"
      ><span class="devsite-nav-text" tooltip>Session management</span></a></li>

  <li class="devsite-nav-item"><a href="/gemini-api/docs/live-api/ephemeral-tokens"
        class="devsite-nav-title"
      ><span class="devsite-nav-text" tooltip>Ephemeral tokens</span></a></li>

  <li class="devsite-nav-item"><a href="/gemini-api/docs/live-api/best-practices"
        class="devsite-nav-title"
      ><span class="devsite-nav-text" tooltip>Best practices</span></a></li>

  <li class="devsite-nav-item
           devsite-nav-heading"><div class="devsite-nav-title devsite-nav-title-no-path">
        <span class="devsite-nav-text" tooltip>Optimization</span>
      </div></li>

  <li class="devsite-nav-item"><a href="/gemini-api/docs/optimization"
        class="devsite-nav-title"
      ><span class="devsite-nav-text" tooltip>Overview</span></a></li>

  <li class="devsite-nav-item"><a href="/gemini-api/docs/batch-api"
        class="devsite-nav-title"
      ><span class="devsite-nav-text" tooltip>Batch API</span></a></li>

  <li class="devsite-nav-item
           devsite-nav-preview"><a href="/gemini-api/docs/webhooks"
        class="devsite-nav-title"
      ><span class="devsite-nav-text" tooltip>Webhooks</span><span class="devsite-nav-icon material-icons"
        data-icon="preview"
        data-title="Preview"
        aria-hidden="true"></span></a></li>

  <li class="devsite-nav-item
           devsite-nav-preview"><a href="/gemini-api/docs/flex-inference"
        class="devsite-nav-title"
      ><span class="devsite-nav-text" tooltip>Flex inference</span><span class="devsite-nav-icon material-icons"
        data-icon="preview"
        data-title="Preview"
        aria-hidden="true"></span></a></li>

  <li class="devsite-nav-item
           devsite-nav-preview"><a href="/gemini-api/docs/priority-inference"
        class="devsite-nav-title"
      ><span class="devsite-nav-text" tooltip>Priority inference</span><span class="devsite-nav-icon material-icons"
        data-icon="preview"
        data-title="Preview"
        aria-hidden="true"></span></a></li>

  <li class="devsite-nav-item"><a href="/gemini-api/docs/caching"
        class="devsite-nav-title"
      ><span class="devsite-nav-text" tooltip>Context caching</span></a></li>

  <li class="devsite-nav-item
           devsite-nav-heading"><div class="devsite-nav-title devsite-nav-title-no-path">
        <span class="devsite-nav-text" tooltip>Guides</span>
      </div></li>

  <li class="devsite-nav-item"><a href="/gemini-api/docs/interactions/streaming"
        class="devsite-nav-title"
      ><span class="devsite-nav-text" tooltip>Streaming</span></a></li>

  <li class="devsite-nav-item
           devsite-nav-expandable"><div class="devsite-expandable-nav">
      <a class="devsite-nav-toggle" aria-hidden="true"></a><div class="devsite-nav-title devsite-nav-title-no-path" tabindex="0" role="button">
        <span class="devsite-nav-text" tooltip>File input</span>
      </div><ul class="devsite-nav-section"><li class="devsite-nav-item"><a href="/gemini-api/docs/file-input-methods"
        class="devsite-nav-title"
      ><span class="devsite-nav-text" tooltip>Input methods</span></a></li><li class="devsite-nav-item"><a href="/gemini-api/docs/files"
        class="devsite-nav-title"
      ><span class="devsite-nav-text" tooltip>Files API</span></a></li></ul></div></li>

  <li class="devsite-nav-item"><a href="/gemini-api/docs/openai"
        class="devsite-nav-title"
      ><span class="devsite-nav-text" tooltip>OpenAI compatibility</span></a></li>

  <li class="devsite-nav-item"><a href="/gemini-api/docs/media-resolution"
        class="devsite-nav-title"
      ><span class="devsite-nav-text" tooltip>Media resolution</span></a></li>

  <li class="devsite-nav-item"><a href="/gemini-api/docs/tokens"
        class="devsite-nav-title"
      ><span class="devsite-nav-text" tooltip>Token counting</span></a></li>

  <li class="devsite-nav-item"><a href="/gemini-api/docs/prompting-strategies"
        class="devsite-nav-title"
      ><span class="devsite-nav-text" tooltip>Prompt engineering</span></a></li>

  <li class="devsite-nav-item
           devsite-nav-expandable"><div class="devsite-expandable-nav">
      <a class="devsite-nav-toggle" aria-hidden="true"></a><div class="devsite-nav-title devsite-nav-title-no-path" tabindex="0" role="button">
        <span class="devsite-nav-text" tooltip>Logs and datasets</span>
      </div><ul class="devsite-nav-section"><li class="devsite-nav-item"><a href="/gemini-api/docs/logs-datasets"
        class="devsite-nav-title"
      ><span class="devsite-nav-text" tooltip>Get started with logs</span></a></li><li class="devsite-nav-item"><a href="/gemini-api/docs/logs-policy"
        class="devsite-nav-title"
      ><span class="devsite-nav-text" tooltip>Data logging and sharing</span></a></li></ul></div></li>

  <li class="devsite-nav-item
           devsite-nav-expandable"><div class="devsite-expandable-nav">
      <a class="devsite-nav-toggle" aria-hidden="true"></a><div class="devsite-nav-title devsite-nav-title-no-path" tabindex="0" role="button">
        <span class="devsite-nav-text" tooltip>Safety</span>
      </div><ul class="devsite-nav-section"><li class="devsite-nav-item"><a href="/gemini-api/docs/safety-settings"
        class="devsite-nav-title"
      ><span class="devsite-nav-text" tooltip>Safety settings</span></a></li><li class="devsite-nav-item"><a href="/gemini-api/docs/safety-guidance"
        class="devsite-nav-title"
      ><span class="devsite-nav-text" tooltip>Safety guidance</span></a></li></ul></div></li>

  <li class="devsite-nav-item
           devsite-nav-expandable"><div class="devsite-expandable-nav">
      <a class="devsite-nav-toggle" aria-hidden="true"></a><div class="devsite-nav-title devsite-nav-title-no-path" tabindex="0" role="button">
        <span class="devsite-nav-text" tooltip>Frameworks</span>
      </div><ul class="devsite-nav-section"><li class="devsite-nav-item"><a href="/gemini-api/docs/langgraph-example"
        class="devsite-nav-title"
      ><span class="devsite-nav-text" tooltip>LangChain &amp; LangGraph</span></a></li><li class="devsite-nav-item"><a href="/gemini-api/docs/crewai-example"
        class="devsite-nav-title"
      ><span class="devsite-nav-text" tooltip>CrewAI</span></a></li><li class="devsite-nav-item"><a href="/gemini-api/docs/llama-index"
        class="devsite-nav-title"
      ><span class="devsite-nav-text" tooltip>LlamaIndex</span></a></li><li class="devsite-nav-item"><a href="/gemini-api/docs/vercel-ai-sdk-example"
        class="devsite-nav-title"
      ><span class="devsite-nav-text" tooltip>Vercel AI SDK</span></a></li><li class="devsite-nav-item"><a href="/gemini-api/docs/temporal-example"
        class="devsite-nav-title"
      ><span class="devsite-nav-text" tooltip>Temporal</span></a></li></ul></div></li>

  <li class="devsite-nav-item
           devsite-nav-heading"><div class="devsite-nav-title devsite-nav-title-no-path">
        <span class="devsite-nav-text" tooltip>Resources</span>
      </div></li>

  <li class="devsite-nav-item"><a href="/gemini-api/docs/changelog"
        class="devsite-nav-title"
      ><span class="devsite-nav-text" tooltip>Release notes</span></a></li>

  <li class="devsite-nav-item"><a href="/gemini-api/docs/deprecations"
        class="devsite-nav-title"
      ><span class="devsite-nav-text" tooltip>Deprecations</span></a></li>

  <li class="devsite-nav-item
           devsite-nav-expandable"><div class="devsite-expandable-nav">
      <a class="devsite-nav-toggle" aria-hidden="true"></a><div class="devsite-nav-title devsite-nav-title-no-path" tabindex="0" role="button">
        <span class="devsite-nav-text" tooltip>Migration</span>
      </div><ul class="devsite-nav-section"><li class="devsite-nav-item"><a href="/gemini-api/docs/migrate"
        class="devsite-nav-title"
      ><span class="devsite-nav-text" tooltip>Migrate to Gen AI SDK</span></a></li><li class="devsite-nav-item"><a href="/gemini-api/docs/migrate-to-interactions"
        class="devsite-nav-title"
      ><span class="devsite-nav-text" tooltip>Migrate to Interactions API</span></a></li><li class="devsite-nav-item"><a href="/gemini-api/docs/interactions-breaking-changes-may-2026"
        class="devsite-nav-title"
      ><span class="devsite-nav-text" tooltip>Interactions breaking changes (May 2026)</span></a></li></ul></div></li>

  <li class="devsite-nav-item"><a href="/gemini-api/docs/rate-limits"
        class="devsite-nav-title"
      ><span class="devsite-nav-text" tooltip>Rate limits</span></a></li>

  <li class="devsite-nav-item"><a href="/gemini-api/docs/billing"
        class="devsite-nav-title"
      ><span class="devsite-nav-text" tooltip>Billing info</span></a></li>

  <li class="devsite-nav-item"><a href="/gemini-api/docs/troubleshooting"
        class="devsite-nav-title"
      ><span class="devsite-nav-text" tooltip>API troubleshooting</span></a></li>

  <li class="devsite-nav-item
           devsite-nav-external"><a href="https://aistudio.google.com/status"
        class="devsite-nav-title"
      ><span class="devsite-nav-text" tooltip>Status</span><span class="devsite-nav-icon material-icons"
        data-icon="external"
        data-title="External"
        aria-hidden="true"></span></a></li>

  <li class="devsite-nav-item"><a href="/gemini-api/docs/partner-integration"
        class="devsite-nav-title"
      ><span class="devsite-nav-text" tooltip>Partner and library integrations</span></a></li>

  <li class="devsite-nav-item
           devsite-nav-expandable"><div class="devsite-expandable-nav">
      <a class="devsite-nav-toggle" aria-hidden="true"></a><div class="devsite-nav-title devsite-nav-title-no-path" tabindex="0" role="button">
        <span class="devsite-nav-text" tooltip>Google AI Studio</span>
      </div><ul class="devsite-nav-section"><li class="devsite-nav-item"><a href="/gemini-api/docs/ai-studio-quickstart"
        class="devsite-nav-title"
      ><span class="devsite-nav-text" tooltip>Quickstart</span></a></li><li class="devsite-nav-item"><a href="/gemini-api/docs/aistudio-build-mode"
        class="devsite-nav-title"
      ><span class="devsite-nav-text" tooltip>Vibe code in Build mode</span></a></li><li class="devsite-nav-item"><a href="/gemini-api/docs/aistudio-fullstack"
        class="devsite-nav-title"
      ><span class="devsite-nav-text" tooltip>Developing Full-Stack Apps</span></a></li><li class="devsite-nav-item"><a href="/gemini-api/docs/aistudio-android"
        class="devsite-nav-title"
      ><span class="devsite-nav-text" tooltip>Build Android Apps</span></a></li><li class="devsite-nav-item"><a href="/gemini-api/docs/aistudio-deploying"
        class="devsite-nav-title"
      ><span class="devsite-nav-text" tooltip>Deploying your app</span></a></li><li class="devsite-nav-item"><a href="/gemini-api/docs/aistudio-agents"
        class="devsite-nav-title"
      ><span class="devsite-nav-text" tooltip>Agents in AI Studio Playground</span></a></li><li class="devsite-nav-item
           devsite-nav-experimental"><a href="/gemini-api/docs/learnlm"
        class="devsite-nav-title"
      ><span class="devsite-nav-text" tooltip>Try out LearnLM</span><span class="devsite-nav-icon material-icons"
        data-icon="experimental"
        data-title="Experimental!"
        aria-hidden="true"></span></a></li><li class="devsite-nav-item"><a href="/gemini-api/docs/troubleshoot-ai-studio"
        class="devsite-nav-title"
      ><span class="devsite-nav-text" tooltip>Troubleshooting</span></a></li><li class="devsite-nav-item"><a href="/gemini-api/docs/workspace"
        class="devsite-nav-title"
      ><span class="devsite-nav-text" tooltip>Access for Workspace users</span></a></li></ul></div></li>

  <li class="devsite-nav-item
           devsite-nav-expandable"><div class="devsite-expandable-nav">
      <a class="devsite-nav-toggle" aria-hidden="true"></a><div class="devsite-nav-title devsite-nav-title-no-path" tabindex="0" role="button">
        <span class="devsite-nav-text" tooltip>Google Cloud Platform</span>
      </div><ul class="devsite-nav-section"><li class="devsite-nav-item"><a href="/gemini-api/docs/migrate-to-cloud"
        class="devsite-nav-title"
      ><span class="devsite-nav-text" tooltip>Gemini Enterprise Agent Platform Gemini API</span></a></li><li class="devsite-nav-item"><a href="/gemini-api/docs/oauth"
        class="devsite-nav-title"
      ><span class="devsite-nav-text" tooltip>OAuth authentication</span></a></li></ul></div></li>

  <li class="devsite-nav-item
           devsite-nav-heading"><div class="devsite-nav-title devsite-nav-title-no-path">
        <span class="devsite-nav-text" tooltip>Policies</span>
      </div></li>

  <li class="devsite-nav-item"><a href="/gemini-api/terms"
        class="devsite-nav-title"
      
        alt-paths=" /gemini-api/docs/zdr "><span class="devsite-nav-text" tooltip>Terms of service</span></a></li>

  <li class="devsite-nav-item"><a href="/gemini-api/docs/available-regions"
        class="devsite-nav-title"
      ><span class="devsite-nav-text" tooltip>Available regions</span></a></li>

  <li class="devsite-nav-item"><a href="/gemini-api/docs/usage-policies"
        class="devsite-nav-title"
      ><span class="devsite-nav-text" tooltip>Abuse monitoring</span></a></li>

  <li class="devsite-nav-item"><a href="/gemini-api/docs/feedback-policies"
        class="devsite-nav-title"
      ><span class="devsite-nav-text" tooltip>Feedback information</span></a></li>
          </ul>
        
        
          
    
  
        
        
          
    
  
    
  
        
      </div>
    
  </div>
</nav>
          
        </devsite-book-nav>
      
      <section id="gc-wrapper">
        <main role="main" id="main-content" class="devsite-main-content"
            
              has-book-nav
              has-sidebar
            >
          <div class="devsite-sidebar">
            <div class="devsite-sidebar-content">
                
                <devsite-toc class="devsite-nav"
                            role="navigation"
                            aria-label="On this page"
                            depth="2"
                            scrollbars
                            data-nosnippet
                  ></devsite-toc>
                <devsite-recommendations-sidebar class="nocontent devsite-nav" data-nosnippet>
                </devsite-recommendations-sidebar>
            </div>
          </div>
          <devsite-content>
            
              










<article class="devsite-article"><style>
      /* Styles inlined from /site-assets/css/style.css */
body[theme="googledevai-theme"] {
  --devsite-background-0: var(--devsite-background-1);
  --devsite-button-border: 1px solid #747775;
  --devsite-button-border-radius: 20rem;
  --devsite-button-font: 500 14px/36px 'Google Sans Text', Roboto, sans-serif;
  --devsite-code-font-family: 'Google Sans Mono', Roboto Mono, monospace;
  --devsite-primary-font-family: 'Google Sans Text', Roboto, sans-serif;
  --devsite-table-heading-font: 500 14px/20px 'Google Sans Text', Roboto, sans-serif;
  --googledevai-border-color: #c4c7c5;
  --googledevai-blue-light: #d7e6ff;
  --googledevai-blue-dark: #2e64de;
  --googledevai-cyan-light: #c7e4ff;
  --googledevai-cyan-dark: #3c8fe3;
  --googledevai-purple-light: #dce2ff;
  --googledevai-purple-dark: #987be9;
  --googledevai-purple: #ac87eb;
  --googledevai-red: #ee4d5d;
  --googledevai-secondary-text: #001d35;
  --googledevai-button-gradient-light: linear-gradient(90deg, var(--googledevai-blue-light), var(--googledevai-cyan-light), var(--googledevai-purple-light));
  --googledevai-button-gradient-dark: linear-gradient(90deg, var(--googledevai-blue), var(--googledevai-cyan), var(--googledevai-purple));
}

body[theme="googledevai-theme"]:not([type="reference"]){
  --googledevai-page-width: 1100px;
}

body[layout=docs][theme="googledevai-theme"]:not([type="reference"]) .devsite-main-content,
body[layout=docs][theme="googledevai-theme"]:not([type="reference"]) .devsite-main-content[has-book-nav][has-sidebar] {
  grid-template-columns: minmax(269px, 1fr) minmax(752px, var(--googledevai-page-width)) minmax(160px, 1fr);
  grid-gap: 3rem;
}

body[layout=docs][theme="googledevai-theme"] devsite-content {
  max-width: var(--googledevai-page-width);
}

body[layout=docs][theme="googledevai-theme"] .devsite-article {
  box-shadow: unset;
}

body[theme="googledevai-theme"] {
  --googledevai-header-gradient: linear-gradient(90deg, var(--googledevai-blue) 50%, var(--googledevai-cyan), var(--googledevai-purple), var(--googledevai-red));
}

body[theme="googledevai-theme"].color-scheme--dark {
  --googledevai-header-gradient: linear-gradient(90deg, var(--googledevai-blue) 75%, var(--googledevai-cyan), var(--googledevai-purple));
  --googledevai-border-color: #444746;
}

/* Ensure that full-bleed pages get the full width. */
body[theme="googledevai-theme"][layout="full"] .devsite-main-content {
  max-width: none;
  padding: 0;
}

/* And ensure that any site banners/ACL warnings/etc don't get hidden on
 * full-bleed pages. */
body[theme="googledevai-theme"][layout="full"] .devsite-banner {
  margin: 0;
}

tab:has(> a.hidden-tab) {
  display: none;
}

body[theme="googledevai-theme"] devsite-toc > .devsite-nav-list {
  border-inline-start: unset;
}

/* Banner notice */
[layout=docs] .devsite-banner:first-of-type {
  background: var(--googledevai-cyan-light);
  border-radius: 10px;
  color: var(--googledevai-secondary-text);
  margin: -2.5rem -0.25rem 2.5rem;
  display: flex;
}

/* Banner notice smaller screens */
@media (max-width: 840px) {
  [layout=docs] .devsite-banner:first-of-type {
    margin: -0.25rem -0.25rem 2.5rem;
  }
}

/* Asides */
.devsite-article-body>aside:not([class*=attempt])  {
  border-radius: 2px;
}

/* Tables */
table:not(.tfo-notebook-buttons) {
  border: 1px solid var(--googledevai-border-color);
  border-collapse: unset;
  border-radius: 9px;
  margin: auto;
  width: 100%;
}

.gemini-api-model-table tr:not(:last-child) td:not(:first-child),
.gemini-api-model-table tr:not(:last-child) th,
th,
table:not(.gemini-api-model-table):not(.tfo-notebook-buttons) tr:not(:last-child) td {
  border-bottom: 1px solid var(--googledevai-border-color);
}

th,
td {
  background: transparent;
  padding: 1rem;
}

/* Notebooks */
devsite-code .tfo-notebook-code-cell-output {
  max-height: 300px;
  overflow: auto;
  background: rgba(237, 247, 255, 1);  /* blue bg to distinguish from input code cells */
}

devsite-code .tfo-notebook-code-cell-output + .devsite-code-buttons-container button {
  background: rgba(237, 247, 255, .7);  /* blue bg to distinguish from input code cells */
}

.color-scheme--dark devsite-code .tfo-notebook-code-cell-output {
  background: rgba(var(--devsite-background-2), 1);
}

.color-scheme--dark devsite-code .tfo-notebook-code-cell-output + .devsite-code-buttons-container button {
  background: rgba(var(--devsite-background-2), .7);
}

devsite-code[dark-code] .tfo-notebook-code-cell-output {
  background: rgba(64, 78, 103, 1);  /* medium slate */
}

devsite-code[dark-code] .tfo-notebook-code-cell-output + .devsite-code-buttons-container button {
  background: rgba(64, 78, 103, .7);  /* medium slate */
}

.devsite-article-body>devsite-code {
  --devsite-code-buttons-container-right: 0;
  --devsite-code-margin: 0 0;
  --devsite-code-padding-block: 14px;
  border-radius: 8px;
}

.devsite-article-body>.beta:not([class*=attempt]),
.devsite-article-body>.caution:not([class*=attempt]),
.devsite-article-body>.deprecated:not([class*=attempt]),
.devsite-article-body>.dogfood:not([class*=attempt]),
.devsite-article-body>.experimental:not([class*=attempt]),
.devsite-article-body>.key-point:not([class*=attempt]),
.devsite-article-body>.key-term:not([class*=attempt]),
.devsite-article-body>.note:not([class*=attempt]),
.devsite-article-body>.objective:not([class*=attempt]),
.devsite-article-body>.preview:not([class*=attempt]),
.devsite-article-body>.special:not([class*=attempt]),
.devsite-article-body>.success:not([class*=attempt]),
.devsite-article-body>.tip:not([class*=attempt]),
.devsite-article-body>.warning:not([class*=attempt]),
.devsite-article-body>aside:not([class*=attempt]) {
  --devsite-notice-margin: 0 0;
  border-radius: 8px;
}

/* override default table styles for notebook buttons */
.devsite-table-wrapper .tfo-notebook-buttons {
  display: block;
  width: auto;
}

.tfo-notebook-buttons td {
  display: inline-block;
  padding: 0 16px 16px 0;
}

/* from DevSite's buttons.scss */
.tfo-notebook-buttons a,
.tfo-notebook-buttons :link,
.tfo-notebook-buttons :visited {
  -moz-appearance: none;
  -webkit-appearance: none;
  -webkit-box-align: center;
  -ms-flex-align: center;
  align-items: center;
  align-self: var(--devsite-button-align-self);
  background: var(--devsite-button-background, var(--devsite-background-1));
  border: var(--devsite-button-border, 0);
  border-radius: var(--devsite-button-border-radius, 2px);
  box-sizing: border-box;
  color: var(--devsite-button-color);
  cursor: pointer;
  display: -webkit-box;
  display: -ms-flexbox;
  display: flex;
  font: var(--devsite-button-font, 500 14px/36px var(--devsite-primary-font-family));
  height: var(--devsite-button-height, 36px);
  letter-spacing: var(--devsite-button-letter-spacing, 0);
  line-height: var(--devsite-button-line-height, 36px);
  margin: var(--devsite-button-margin, 0);
  margin-inline-end: var(--devsite-button-margin-x-end);
  max-width: var(--devsite-button-max-width, none);
  min-width: 36px;
  outline: 0;
  overflow: hidden;
  padding: var(--devsite-button-with-icon-padding, 0 16px);
  text-align: center;
  text-decoration: none;
  text-overflow: ellipsis;
  text-transform: var(--devsite-button-text-transform, uppercase);
  transition:
    background-color .2s,
    border .2s;
  vertical-align: middle;
  white-space: nowrap;
  width: var(--devsite-button-width, auto);
}

.tfo-notebook-buttons a:hover,
.tfo-notebook-buttons a:focus {
  background: var(--devsite-button-background-hover);
  border: var(--devsite-button-border-hover, 0);
  color: var(--devsite-button-color-hover, var(--devsite-button-color));
  text-decoration: var(--devsite-button-text-decoration-hover, none);
}

.tfo-notebook-buttons a:active {
  background: var(--devsite-button-background-active);
  border: var(--devsite-button-border-active, 0);
  transform: var(--devsite-button-transform-active, none);
}

.tfo-notebook-buttons tr {
  background: 0;
  border: 0;
}

/* on rendered notebook page,
   remove link to webpage since we're already here */
.tfo-notebook-buttons:not(.tfo-api) td:first-child {
  display: none;
}

.tfo-notebook-buttons td > a > img {
  margin: 0 8px 0 -4px;
  height: 20px;
}

[appearance='dark'] .tfo-notebook-buttons td > a > img {
  filter: invert(1);
}

@media (prefers-color-scheme: dark) {
  [appearance='device'] .tfo-notebook-buttons td > a > img {
    filter: invert(1);
  }
  .sub-heading {
    background-color: #333;
    color: #bdbdbd;
  }
}

[appearance='dark'] .sub-heading {
  background-color: #333;
  color: #bdbdbd;
}

.sub-heading {
  background-color: #f2f2f2;
  color: #5f6368;
}

@media screen and (max-width: 600px) {
  .tfo-notebook-buttons td {
    display: block;
  }
}

devsite-nav-buttons button {
  margin-left: 0;
  margin-top: 5px;
}

code {
  border-radius: 6px
}

devsite-book-nav .devsite-nav-list>.devsite-nav-heading:not(.devsite-nav-divider) {
  border-top: 0;
  padding-bottom: 0.9rem;
  font-size: 1rem;
}

/*
 * TODO(b/439059414): Remove this workaround in favor of a project-level
 * body_class when possible.
 */
.ais-theme-marker {
  display: none;
}

/*
 * Gemini API body class.
 * https://source.corp.google.com/piper///depot/google3/third_party/devsite/googledevai/en/gemini-api/_project.yaml;l=7
 */
.gemini-api devsite-thumb-rating[position="header"],
.gemini-api devsite-feedback[position="header"] {
  /* Hide the thumb rating and feedback widgets at the top of the page. */
  display: none;
}

/*
 * Shaded table styles look like a .pricing-table but are more flexible around
 * content sizes in each column.
 */
.shaded-table {
  border-collapse: separate;
  border-spacing: 0;
  border-radius: 8px;
  overflow: hidden;
}

.shaded-table th {
  background-color: #f2f2f2;
  text-align: left;
  padding: 8px;
}

/* These should use theme colours for light too, so we don't
 * need an override. */
.color-scheme--dark .shaded-table th {
  background-color: var(--devsite-ref-palette--grey800);
}

.shaded-table td {
    padding: 8px;
}

.shaded-table th:first-child {
  border-top-left-radius: 8px;
}

.shaded-table th:last-child {
  border-top-right-radius: 8px;
}

.shaded-table tr:last-child td:first-child {
  border-bottom-left-radius: 8px;
}

.shaded-table tr:last-child td:last-child {
  border-bottom-right-radius: 8px;
}

.devsite-nav {
    font-size: var(--devsite-nav-font-size, 14px);
}

.devsite-nav-item {
    line-height: var(--devsite-nav-item-line-height, 20px);
}

.devsite-book-nav-bg, devsite-book-nav {
    width: 210px;
    scrollbar-width: thin;
}

/* Hide the old toggle button immediately */
.devsite-expandable-nav > .devsite-nav-toggle {
    display: none !important;
}

/* Ion setup: Default State (Chevron Right) */
.devsite-expandable-nav > .devsite-nav-title::after {
    font-family: 'Material Icons';
    font-weight: normal;
    font-style: normal;
    font-size: 18px;
    line-height: 1;
    color: #888;
    /* Default: Chevron Right */
    content: "\e5cc";
    flex-shrink: 0;
    margin-left: 8px;
}

/* Down state logic */
.devsite-expandable-nav.expanded > .devsite-nav-title::after,
.devsite-expandable-nav:has(.devsite-nav-active) > .devsite-nav-title::after,
.devsite-expandable-nav > .devsite-nav-title[aria-expanded="true"]::after {
    content: "\e313";
}

/* Close state logic */
.devsite-expandable-nav > .devsite-nav-title[aria-expanded="false"]::after {
    content: "\e5cc" !important;
}

/* Hovercard styling */
.gemini-api .heading:has(devsite-gemini-api-hovercard-button) {
  display: flex;
  justify-content: space-between;
  align-items: center;
}

.gemini-api .heading:has(devsite-gemini-api-hovercard-button) h1 {
  margin-bottom: 0;
}

devsite-gemini-api-hovercard,
devsite-gemini-api-hovercard-button {
  /* Render above any code blocks on the page */
  z-index: 1;
}

.devsite-nav-icon[data-icon="beta"], .devsite-nav-icon[data-icon="preview"],
.devsite-nav-icon[data-icon="experimental"] {
  margin: -5px 0 -1px 4px;
}
      </style><style>
      /* Styles inlined from /site-assets/css/pricing.css */
/* Pricing table styles */

.pricing-table {
  border-collapse: separate;
  border-spacing: 0;
  border-radius: 8px;
  overflow: hidden;
}

.pricing-table th {
  background-color: #f2f2f2;
  text-align: left;
  padding: 8px;
}

/* Set the second and after (of three total) columns to 35% width. */
.pricing-table th:nth-child(n+2) {
  width: 35%;
}

/* These should use theme colours for light too, so we don't
 * need an override. */
.color-scheme--dark .pricing-table th {
  background-color: var(--devsite-ref-palette--grey800);
}

.pricing-table td {
    padding: 8px;
}

.free-tier {
  background-color: none;
}

.paid-tier {
  background-color: #eff5ff;
}

.color-scheme--dark .paid-tier {
  background-color: var(--devsite-background-5);
}

.pricing-table th:first-child {
  border-top-left-radius: 8px;
}

.pricing-table th:last-child {
  border-top-right-radius: 8px;
}

.pricing-table tr:last-child td:first-child {
  border-bottom-left-radius: 8px;
}

.pricing-table tr:last-child td:last-child {
  border-bottom-right-radius: 8px;
}

.pricing-container {
    max-width: 1100px;
    width: 100%;
}

.pricing-cards {
    display: grid;
    grid-template-columns: repeat(auto-fit, minmax(300px, 1fr));
    gap: 2rem;
    justify-content: center;
}

.pricing-card {
    background-color: #ffffff;
    border-radius: 16px; 
    border: 1px solid #dadce0;
    padding: 2.5rem;
    display: flex;
    flex-direction: column; 
    transition: all 0.3s ease;
    position: relative; 
}

.color-scheme--dark .pricing-card {
  background-color: var(--devsite-ref-palette--grey800);
}

.plan-name {
    font-size: 1.75rem;
    font-weight: 700; 
    margin: 0 0 0.5rem 0;
}

.plan-description {
    font-size: 1rem;
    color: #5f6368;
    margin: 0 0 2.5rem 0;
    line-height: 1.5;
    min-height: 80px;
}

.color-scheme--dark .plan-description {
  color: var(--devsite-primary-text-color);
}

.plan-description a {
    color: #1a73e8;
    text-decoration: none;
}
.plan-description a:hover {
    text-decoration: underline;
}

.features {
    list-style: none;
    padding: 0;
    margin: 0 0 2rem 0;
}

.features li {
    display: flex;
    align-items: flex-start;
    margin-bottom: 1.25rem;
    font-size: 1rem;
    line-height: 1.5;
    color: #3c4043;
}

.features li.feature-description {
    display: block;
    color: #5f6368;
}

.features li a {
    color: #1a73e8;
    text-decoration: none;
    margin-left: 4px;
}

.features li .material-symbols-outlined {
    font-size: 24px;
    margin-right: 0.75rem;
    color: #3c4043;
    margin-top: 2px;
}

.color-scheme--dark .features li,
.features li .material-symbols-outlined {
  color: var(--devsite-primary-text-color);
}

.cta-button {
    display: inline-block;
    text-align: center;
    text-decoration: none;
    width: 100%;
    padding: 0.75rem 1rem;
    border-radius: 8px;
    font-size: 1rem;
    font-weight: 500;
    cursor: pointer;
    transition: background-color 0.2s ease;
    box-sizing: border-box;
    border: 1px solid #dadce0;
    background-color: #fff;
    color: #1a73e8;
    margin-top: auto;
}

.cta-button:hover {
    background-color: rgba(66, 133, 244, 0.05); 
}

.pricing-card.recommended {
    border: 2px solid #1a73e8;
    overflow: hidden; 
}

.pricing-card.recommended::before {
    position: absolute;
    top: 22px;
    right: -32px;
    width: 120px;
    height: 30px;
    background-color: #1a73e8;
    color: white;
    display: flex;
    justify-content: center;
    align-items: center;
    font-size: 0.8rem;
    font-weight: 600;
    transform: rotate(45deg);
    z-index: 1; 
}

.heading-group {
    display: flex;
    flex-direction: column;
}

.heading-group h2 {
    margin-bottom: 0;
}

.heading-group em {
    margin-top: 0;
}

.row-gray {
  background-color: #f2f2f2; /* Light gray */
  color: #666666;
  font-style: italic;
}

.row-gray code {
  font-style: italic;
}

      </style>
  
  
  
    <div class="devsite-banner devsite-banner-announcement nocontent" data-nosnippet
      
        
    background="google-blue"
  
      >
      <div class="devsite-banner-message">
        <div class="devsite-banner-message-text">
          <a href="/gemini-api/docs/deep-research" style="color: black;">Gemini Deep Research</a> is now available in preview with collaborative planning, visualization, MCP support, and more.
        </div>
      </div>
    </div>
  
  
  

  <div class="devsite-article-meta nocontent" role="navigation" data-nosnippet>
    
    
    <ul class="devsite-breadcrumb-list"
  
    aria-label="Breadcrumb">
  
  <li class="devsite-breadcrumb-item
             ">
    
    
    
      
        
  <a href="https://ai.google.dev/"
      
        class="devsite-breadcrumb-link gc-analytics-event"
      
        data-category="Site-Wide Custom Events"
      
        data-label="Breadcrumbs"
      
        data-value="1"
      
        track-type="globalNav"
      
        track-name="breadcrumb"
      
        track-metadata-position="1"
      
        track-metadata-eventdetail=""
      
    >
    
          Home
        
  </a>
  
      
    
  </li>
  
  <li class="devsite-breadcrumb-item
             ">
    
      
      <div class="devsite-breadcrumb-guillemet material-icons" aria-hidden="true"></div>
    
    
    
      
        
  <a href="https://ai.google.dev/gemini-api"
      
        class="devsite-breadcrumb-link gc-analytics-event"
      
        data-category="Site-Wide Custom Events"
      
        data-label="Breadcrumbs"
      
        data-value="2"
      
        track-type="globalNav"
      
        track-name="breadcrumb"
      
        track-metadata-position="2"
      
        track-metadata-eventdetail="Gemini API"
      
    >
    
          Gemini API
        
  </a>
  
      
    
  </li>
  
  <li class="devsite-breadcrumb-item
             ">
    
      
      <div class="devsite-breadcrumb-guillemet material-icons" aria-hidden="true"></div>
    
    
    
      
        
  <a href="https://ai.google.dev/gemini-api/docs/generate-content"
      
        class="devsite-breadcrumb-link gc-analytics-event"
      
        data-category="Site-Wide Custom Events"
      
        data-label="Breadcrumbs"
      
        data-value="3"
      
        track-type="globalNav"
      
        track-name="breadcrumb"
      
        track-metadata-position="3"
      
        track-metadata-eventdetail="Gemini API"
      
    >
    
          generateContent API
        
  </a>
  
      
    
  </li>
  
  <li class="devsite-breadcrumb-item
             ">
    
      
      <div class="devsite-breadcrumb-guillemet material-icons" aria-hidden="true"></div>
    
    
    
      
        
  <a href="https://ai.google.dev/gemini-api/docs"
      
        class="devsite-breadcrumb-link gc-analytics-event"
      
        data-category="Site-Wide Custom Events"
      
        data-label="Breadcrumbs"
      
        data-value="4"
      
        track-type="globalNav"
      
        track-name="breadcrumb"
      
        track-metadata-position="4"
      
        track-metadata-eventdetail=""
      
    >
    
          Docs
        
  </a>
  
      
    
  </li>
  
</ul>
    
      
    <devsite-thumb-rating position="header">
    </devsite-thumb-rating>
  
    
    <devsite-gemini-api-switcher class="nocontent"></devsite-gemini-api-switcher>
  </div>
  
    <devsite-feedback
  position="header"
  project-name="Gemini API"
  product-id="5292923"
  bucket="documentation"
  context=""
  version="t-devsite-webserver-20260528-r00-rc00.477908439157110416"
  data-label="Send Feedback Button"
  track-type="feedback"
  track-name="sendFeedbackLink"
  track-metadata-position="header"
  class="nocontent"
  data-nosnippet
  
  
  
    project-icon="https://www.gstatic.com/devrel-devsite/prod/v5b93ab110c02dc91cc5b79fb160a3c37758bb2dfb04b22b9173ffe5646621934/googledevai/images/touchicon-180-new.png"
  
  
  
  >

  <button>
  
    
    Send feedback
  
  </button>
</devsite-feedback>
  <devsite-actions hidden data-nosnippet>
    <devsite-llm-tools></devsite-llm-tools></devsite-actions>
  
    
  

  <devsite-toc class="devsite-nav"
    depth="2"
    devsite-toc-embedded
    >
  </devsite-toc>
  
    
  <div class="devsite-article-body clearfix
  devsite-no-page-title">

  
    
    


<p>
</p>

<div id="gemini-api-switcher-trigger" style="display:none;"></div>

<p></p>

<h1 class="devsite-page-title" id="text-to-speech-generation-tts" data-text="Text-to-speech generation (TTS)" tabindex="-1">Text-to-speech generation (TTS)</h1>

<p>The Gemini API can transform text input into single speaker or multi-speaker
audio using Gemini text-to-speech (TTS) generation capabilities.
Text-to-speech (TTS) generation is <em><a href="#controllable">controllable</a></em>,
meaning you can use natural language to structure interactions and guide the
<em>style</em>, <em>accent</em>, <em>pace</em>, and <em>tone</em> of the audio.</p>

<div style="text-align: center;">
  <a href="https://aistudio.google.com/apps/bundled/voice-library?showPreview=truew" class="button button-primary">Try in Google AI Studio</a>
</div>

<p>The TTS capability differs from speech generation provided through the
<a href="/gemini-api/docs/live">Live API</a>, which is designed for interactive,
unstructured audio, and multimodal inputs and outputs. While the Live API excels
in dynamic conversational contexts, TTS through the Gemini API
is tailored for scenarios that require exact text recitation with fine-grained
control over style and sound, such as podcast or audiobook generation.</p>

<p>This guide shows you how to generate single-speaker and multi-speaker audio from
text.</p>
<aside class="preview"><strong>Preview:</strong><span> Gemini text-to-speech (TTS) is in
<a href="/gemini-api/docs/models#preview">Preview</a>.</span></aside>
<h2 id="before-you-begin" class="hide-from-toc" data-text="Before you begin" tabindex="-1">Before you begin</h2>

<p>Ensure you use a Gemini model variant with Gemini text-to-speech (TTS)
capabilities, as listed in the <a href="/gemini-api/docs/speech-generation#supported-models">Supported models</a> section. For optimal
results, consider which model best fits your specific use case.</p>

<p>You may find it useful to <a href="https://aistudio.google.com/generate-speech">test the Gemini TTS models in AI Studio</a> before you start building.</p>
<aside class="note"><strong>Note:</strong><span> TTS models accept text-only inputs and produce audio-only outputs. For a
complete list of restrictions specific to TTS models, review the <a href="/gemini-api/docs/speech-generation#limitations">Limitations</a> section.</span></aside>
<h2 id="single-speaker" data-text="Single-speaker TTS" tabindex="-1">Single-speaker TTS</h2>

<p>To convert text to single-speaker audio, set the response modality to &quot;audio&quot;,
and pass a <code translate="no" dir="ltr">SpeechConfig</code> object with <code translate="no" dir="ltr">VoiceConfig</code> set.
You&#39;ll need to choose a voice name from the prebuilt <a href="#voices">output voices</a>.</p>

<p>This example saves the output audio from the model in a wave file:</p>
<div><devsite-selector data-ds-scope="code-sample">
<section><h3 id="python" data-text="Python" tabindex="-1">Python</h3><div></div><devsite-code><pre class="devsite-click-to-copy" translate="no" dir="ltr" is-upgraded syntax="Python"><code translate="no" dir="ltr"><span class="devsite-syntax-kn">from</span><span class="devsite-syntax-w"> </span><span class="devsite-syntax-nn">google</span><span class="devsite-syntax-w"> </span><span class="devsite-syntax-kn">import</span> <span class="devsite-syntax-n">genai</span>
<span class="devsite-syntax-kn">from</span><span class="devsite-syntax-w"> </span><span class="devsite-syntax-nn">google.genai</span><span class="devsite-syntax-w"> </span><span class="devsite-syntax-kn">import</span> <span class="devsite-syntax-n">types</span>
<span class="devsite-syntax-kn">import</span><span class="devsite-syntax-w"> </span><span class="devsite-syntax-nn">wave</span>

<span class="devsite-syntax-c1"># Set up the wave file to save the output:</span>
<span class="devsite-syntax-k">def</span><span class="devsite-syntax-w"> </span><span class="devsite-syntax-nf">wave_file</span><span class="devsite-syntax-p">(</span><span class="devsite-syntax-n">filename</span><span class="devsite-syntax-p">,</span> <span class="devsite-syntax-n">pcm</span><span class="devsite-syntax-p">,</span> <span class="devsite-syntax-n">channels</span><span class="devsite-syntax-o">=</span><span class="devsite-syntax-mi">1</span><span class="devsite-syntax-p">,</span> <span class="devsite-syntax-n">rate</span><span class="devsite-syntax-o">=</span><span class="devsite-syntax-mi">24000</span><span class="devsite-syntax-p">,</span> <span class="devsite-syntax-n">sample_width</span><span class="devsite-syntax-o">=</span><span class="devsite-syntax-mi">2</span><span class="devsite-syntax-p">):</span>
   <span class="devsite-syntax-k">with</span> <span class="devsite-syntax-n">wave</span><span class="devsite-syntax-o">.</span><span class="devsite-syntax-n">open</span><span class="devsite-syntax-p">(</span><span class="devsite-syntax-n">filename</span><span class="devsite-syntax-p">,</span> <span class="devsite-syntax-s2">"wb"</span><span class="devsite-syntax-p">)</span> <span class="devsite-syntax-k">as</span> <span class="devsite-syntax-n">wf</span><span class="devsite-syntax-p">:</span>
      <span class="devsite-syntax-n">wf</span><span class="devsite-syntax-o">.</span><span class="devsite-syntax-n">setnchannels</span><span class="devsite-syntax-p">(</span><span class="devsite-syntax-n">channels</span><span class="devsite-syntax-p">)</span>
      <span class="devsite-syntax-n">wf</span><span class="devsite-syntax-o">.</span><span class="devsite-syntax-n">setsampwidth</span><span class="devsite-syntax-p">(</span><span class="devsite-syntax-n">sample_width</span><span class="devsite-syntax-p">)</span>
      <span class="devsite-syntax-n">wf</span><span class="devsite-syntax-o">.</span><span class="devsite-syntax-n">setframerate</span><span class="devsite-syntax-p">(</span><span class="devsite-syntax-n">rate</span><span class="devsite-syntax-p">)</span>
      <span class="devsite-syntax-n">wf</span><span class="devsite-syntax-o">.</span><span class="devsite-syntax-n">writeframes</span><span class="devsite-syntax-p">(</span><span class="devsite-syntax-n">pcm</span><span class="devsite-syntax-p">)</span>

<span class="devsite-syntax-n">client</span> <span class="devsite-syntax-o">=</span> <span class="devsite-syntax-n">genai</span><span class="devsite-syntax-o">.</span><span class="devsite-syntax-n">Client</span><span class="devsite-syntax-p">()</span>

<span class="devsite-syntax-n">response</span> <span class="devsite-syntax-o">=</span> <span class="devsite-syntax-n">client</span><span class="devsite-syntax-o">.</span><span class="devsite-syntax-n">models</span><span class="devsite-syntax-o">.</span><span class="devsite-syntax-n">generate_content</span><span class="devsite-syntax-p">(</span>
   <span class="devsite-syntax-n">model</span><span class="devsite-syntax-o">=</span><span class="devsite-syntax-s2">"gemini-3.1-flash-tts-preview"</span><span class="devsite-syntax-p">,</span>
   <span class="devsite-syntax-n">contents</span><span class="devsite-syntax-o">=</span><span class="devsite-syntax-s2">"Say cheerfully: Have a wonderful day!"</span><span class="devsite-syntax-p">,</span>
   <span class="devsite-syntax-n">config</span><span class="devsite-syntax-o">=</span><span class="devsite-syntax-n">types</span><span class="devsite-syntax-o">.</span><span class="devsite-syntax-n">GenerateContentConfig</span><span class="devsite-syntax-p">(</span>
      <span class="devsite-syntax-n">response_modalities</span><span class="devsite-syntax-o">=</span><span class="devsite-syntax-p">[</span><span class="devsite-syntax-s2">"AUDIO"</span><span class="devsite-syntax-p">],</span>
      <span class="devsite-syntax-n">speech_config</span><span class="devsite-syntax-o">=</span><span class="devsite-syntax-n">types</span><span class="devsite-syntax-o">.</span><span class="devsite-syntax-n">SpeechConfig</span><span class="devsite-syntax-p">(</span>
         <span class="devsite-syntax-n">voice_config</span><span class="devsite-syntax-o">=</span><span class="devsite-syntax-n">types</span><span class="devsite-syntax-o">.</span><span class="devsite-syntax-n">VoiceConfig</span><span class="devsite-syntax-p">(</span>
            <span class="devsite-syntax-n">prebuilt_voice_config</span><span class="devsite-syntax-o">=</span><span class="devsite-syntax-n">types</span><span class="devsite-syntax-o">.</span><span class="devsite-syntax-n">PrebuiltVoiceConfig</span><span class="devsite-syntax-p">(</span>
               <span class="devsite-syntax-n">voice_name</span><span class="devsite-syntax-o">=</span><span class="devsite-syntax-s1">'Kore'</span><span class="devsite-syntax-p">,</span>
            <span class="devsite-syntax-p">)</span>
         <span class="devsite-syntax-p">)</span>
      <span class="devsite-syntax-p">),</span>
   <span class="devsite-syntax-p">)</span>
<span class="devsite-syntax-p">)</span>

<span class="devsite-syntax-n">data</span> <span class="devsite-syntax-o">=</span> <span class="devsite-syntax-n">response</span><span class="devsite-syntax-o">.</span><span class="devsite-syntax-n">candidates</span><span class="devsite-syntax-p">[</span><span class="devsite-syntax-mi">0</span><span class="devsite-syntax-p">]</span><span class="devsite-syntax-o">.</span><span class="devsite-syntax-n">content</span><span class="devsite-syntax-o">.</span><span class="devsite-syntax-n">parts</span><span class="devsite-syntax-p">[</span><span class="devsite-syntax-mi">0</span><span class="devsite-syntax-p">]</span><span class="devsite-syntax-o">.</span><span class="devsite-syntax-n">inline_data</span><span class="devsite-syntax-o">.</span><span class="devsite-syntax-n">data</span>

<span class="devsite-syntax-n">file_name</span><span class="devsite-syntax-o">=</span><span class="devsite-syntax-s1">'out.wav'</span>
<span class="devsite-syntax-n">wave_file</span><span class="devsite-syntax-p">(</span><span class="devsite-syntax-n">file_name</span><span class="devsite-syntax-p">,</span> <span class="devsite-syntax-n">data</span><span class="devsite-syntax-p">)</span> <span class="devsite-syntax-c1"># Saves the file to current directory</span>
</code></pre></devsite-code>
<div>
  <aside class="objective">
     <p>For more code samples, refer to the
     "TTS - Get Started" file in the cookbooks repository:
     </p>
     <p>
        <a href="https://colab.research.google.com/github/google-gemini/cookbook/blob/main/quickstarts/Get_started_TTS.ipynb" track-type="notebookTutorial" track-name="gitHubLink">View
        on GitHub</a>
     </p>
  </aside>
</div></section>
<section><h3 id="javascript" data-text="JavaScript" tabindex="-1">JavaScript</h3><div></div><devsite-code><pre class="devsite-click-to-copy" translate="no" dir="ltr" is-upgraded syntax="JavaScript"><code translate="no" dir="ltr"><span class="devsite-syntax-k">import</span><span class="devsite-syntax-w"> </span><span class="devsite-syntax-p">{</span><span class="devsite-syntax-nx">GoogleGenAI</span><span class="devsite-syntax-p">}</span><span class="devsite-syntax-w"> </span><span class="devsite-syntax-kr">from</span><span class="devsite-syntax-w"> </span><span class="devsite-syntax-s1">'@google/genai'</span><span class="devsite-syntax-p">;</span>
<span class="devsite-syntax-k">import</span><span class="devsite-syntax-w"> </span><span class="devsite-syntax-nx">wav</span><span class="devsite-syntax-w"> </span><span class="devsite-syntax-kr">from</span><span class="devsite-syntax-w"> </span><span class="devsite-syntax-s1">'wav'</span><span class="devsite-syntax-p">;</span>

<span class="devsite-syntax-k">async</span><span class="devsite-syntax-w"> </span><span class="devsite-syntax-kd">function</span><span class="devsite-syntax-w"> </span><span class="devsite-syntax-nx">saveWaveFile</span><span class="devsite-syntax-p">(</span>
<span class="devsite-syntax-w">   </span><span class="devsite-syntax-nx">filename</span><span class="devsite-syntax-p">,</span>
<span class="devsite-syntax-w">   </span><span class="devsite-syntax-nx">pcmData</span><span class="devsite-syntax-p">,</span>
<span class="devsite-syntax-w">   </span><span class="devsite-syntax-nx">channels</span><span class="devsite-syntax-w"> </span><span class="devsite-syntax-o">=</span><span class="devsite-syntax-w"> </span><span class="devsite-syntax-mf">1</span><span class="devsite-syntax-p">,</span>
<span class="devsite-syntax-w">   </span><span class="devsite-syntax-nx">rate</span><span class="devsite-syntax-w"> </span><span class="devsite-syntax-o">=</span><span class="devsite-syntax-w"> </span><span class="devsite-syntax-mf">24000</span><span class="devsite-syntax-p">,</span>
<span class="devsite-syntax-w">   </span><span class="devsite-syntax-nx">sampleWidth</span><span class="devsite-syntax-w"> </span><span class="devsite-syntax-o">=</span><span class="devsite-syntax-w"> </span><span class="devsite-syntax-mf">2</span><span class="devsite-syntax-p">,</span>
<span class="devsite-syntax-p">)</span><span class="devsite-syntax-w"> </span><span class="devsite-syntax-p">{</span>
<span class="devsite-syntax-w">   </span><span class="devsite-syntax-k">return</span><span class="devsite-syntax-w"> </span><span class="devsite-syntax-ow">new</span><span class="devsite-syntax-w"> </span><span class="devsite-syntax-nb">Promise</span><span class="devsite-syntax-p">((</span><span class="devsite-syntax-nx">resolve</span><span class="devsite-syntax-p">,</span><span class="devsite-syntax-w"> </span><span class="devsite-syntax-nx">reject</span><span class="devsite-syntax-p">)</span><span class="devsite-syntax-w"> </span><span class="devsite-syntax-o">=</span>&gt;<span class="devsite-syntax-w"> </span><span class="devsite-syntax-p">{</span>
<span class="devsite-syntax-w">      </span><span class="devsite-syntax-kd">const</span><span class="devsite-syntax-w"> </span><span class="devsite-syntax-nx">writer</span><span class="devsite-syntax-w"> </span><span class="devsite-syntax-o">=</span><span class="devsite-syntax-w"> </span><span class="devsite-syntax-ow">new</span><span class="devsite-syntax-w"> </span><span class="devsite-syntax-nx">wav</span><span class="devsite-syntax-p">.</span><span class="devsite-syntax-nx">FileWriter</span><span class="devsite-syntax-p">(</span><span class="devsite-syntax-nx">filename</span><span class="devsite-syntax-p">,</span><span class="devsite-syntax-w"> </span><span class="devsite-syntax-p">{</span>
<span class="devsite-syntax-w">            </span><span class="devsite-syntax-nx">channels</span><span class="devsite-syntax-p">,</span>
<span class="devsite-syntax-w">            </span><span class="devsite-syntax-nx">sampleRate</span><span class="devsite-syntax-o">:</span><span class="devsite-syntax-w"> </span><span class="devsite-syntax-nx">rate</span><span class="devsite-syntax-p">,</span>
<span class="devsite-syntax-w">            </span><span class="devsite-syntax-nx">bitDepth</span><span class="devsite-syntax-o">:</span><span class="devsite-syntax-w"> </span><span class="devsite-syntax-nx">sampleWidth</span><span class="devsite-syntax-w"> </span><span class="devsite-syntax-o">*</span><span class="devsite-syntax-w"> </span><span class="devsite-syntax-mf">8</span><span class="devsite-syntax-p">,</span>
<span class="devsite-syntax-w">      </span><span class="devsite-syntax-p">});</span>

<span class="devsite-syntax-w">      </span><span class="devsite-syntax-nx">writer</span><span class="devsite-syntax-p">.</span><span class="devsite-syntax-nx">on</span><span class="devsite-syntax-p">(</span><span class="devsite-syntax-s1">'finish'</span><span class="devsite-syntax-p">,</span><span class="devsite-syntax-w"> </span><span class="devsite-syntax-nx">resolve</span><span class="devsite-syntax-p">);</span>
<span class="devsite-syntax-w">      </span><span class="devsite-syntax-nx">writer</span><span class="devsite-syntax-p">.</span><span class="devsite-syntax-nx">on</span><span class="devsite-syntax-p">(</span><span class="devsite-syntax-s1">'error'</span><span class="devsite-syntax-p">,</span><span class="devsite-syntax-w"> </span><span class="devsite-syntax-nx">reject</span><span class="devsite-syntax-p">);</span>

<span class="devsite-syntax-w">      </span><span class="devsite-syntax-nx">writer</span><span class="devsite-syntax-p">.</span><span class="devsite-syntax-nx">write</span><span class="devsite-syntax-p">(</span><span class="devsite-syntax-nx">pcmData</span><span class="devsite-syntax-p">);</span>
<span class="devsite-syntax-w">      </span><span class="devsite-syntax-nx">writer</span><span class="devsite-syntax-p">.</span><span class="devsite-syntax-nx">end</span><span class="devsite-syntax-p">();</span>
<span class="devsite-syntax-w">   </span><span class="devsite-syntax-p">});</span>
<span class="devsite-syntax-p">}</span>

<span class="devsite-syntax-k">async</span><span class="devsite-syntax-w"> </span><span class="devsite-syntax-kd">function</span><span class="devsite-syntax-w"> </span><span class="devsite-syntax-nx">main</span><span class="devsite-syntax-p">()</span><span class="devsite-syntax-w"> </span><span class="devsite-syntax-p">{</span>
<span class="devsite-syntax-w">   </span><span class="devsite-syntax-kd">const</span><span class="devsite-syntax-w"> </span><span class="devsite-syntax-nx">ai</span><span class="devsite-syntax-w"> </span><span class="devsite-syntax-o">=</span><span class="devsite-syntax-w"> </span><span class="devsite-syntax-ow">new</span><span class="devsite-syntax-w"> </span><span class="devsite-syntax-nx">GoogleGenAI</span><span class="devsite-syntax-p">({});</span>

<span class="devsite-syntax-w">   </span><span class="devsite-syntax-kd">const</span><span class="devsite-syntax-w"> </span><span class="devsite-syntax-nx">response</span><span class="devsite-syntax-w"> </span><span class="devsite-syntax-o">=</span><span class="devsite-syntax-w"> </span><span class="devsite-syntax-k">await</span><span class="devsite-syntax-w"> </span><span class="devsite-syntax-nx">ai</span><span class="devsite-syntax-p">.</span><span class="devsite-syntax-nx">models</span><span class="devsite-syntax-p">.</span><span class="devsite-syntax-nx">generateContent</span><span class="devsite-syntax-p">({</span>
<span class="devsite-syntax-w">      </span><span class="devsite-syntax-nx">model</span><span class="devsite-syntax-o">:</span><span class="devsite-syntax-w"> </span><span class="devsite-syntax-s2">"gemini-3.1-flash-tts-preview"</span><span class="devsite-syntax-p">,</span>
<span class="devsite-syntax-w">      </span><span class="devsite-syntax-nx">contents</span><span class="devsite-syntax-o">:</span><span class="devsite-syntax-w"> </span><span class="devsite-syntax-p">[{</span><span class="devsite-syntax-w"> </span><span class="devsite-syntax-nx">parts</span><span class="devsite-syntax-o">:</span><span class="devsite-syntax-w"> </span><span class="devsite-syntax-p">[{</span><span class="devsite-syntax-w"> </span><span class="devsite-syntax-nx">text</span><span class="devsite-syntax-o">:</span><span class="devsite-syntax-w"> </span><span class="devsite-syntax-s1">'Say cheerfully: Have a wonderful day!'</span><span class="devsite-syntax-w"> </span><span class="devsite-syntax-p">}]</span><span class="devsite-syntax-w"> </span><span class="devsite-syntax-p">}],</span>
<span class="devsite-syntax-w">      </span><span class="devsite-syntax-nx">config</span><span class="devsite-syntax-o">:</span><span class="devsite-syntax-w"> </span><span class="devsite-syntax-p">{</span>
<span class="devsite-syntax-w">            </span><span class="devsite-syntax-nx">responseModalities</span><span class="devsite-syntax-o">:</span><span class="devsite-syntax-w"> </span><span class="devsite-syntax-p">[</span><span class="devsite-syntax-s1">'AUDIO'</span><span class="devsite-syntax-p">],</span>
<span class="devsite-syntax-w">            </span><span class="devsite-syntax-nx">speechConfig</span><span class="devsite-syntax-o">:</span><span class="devsite-syntax-w"> </span><span class="devsite-syntax-p">{</span>
<span class="devsite-syntax-w">               </span><span class="devsite-syntax-nx">voiceConfig</span><span class="devsite-syntax-o">:</span><span class="devsite-syntax-w"> </span><span class="devsite-syntax-p">{</span>
<span class="devsite-syntax-w">                  </span><span class="devsite-syntax-nx">prebuiltVoiceConfig</span><span class="devsite-syntax-o">:</span><span class="devsite-syntax-w"> </span><span class="devsite-syntax-p">{</span><span class="devsite-syntax-w"> </span><span class="devsite-syntax-nx">voiceName</span><span class="devsite-syntax-o">:</span><span class="devsite-syntax-w"> </span><span class="devsite-syntax-s1">'Kore'</span><span class="devsite-syntax-w"> </span><span class="devsite-syntax-p">},</span>
<span class="devsite-syntax-w">               </span><span class="devsite-syntax-p">},</span>
<span class="devsite-syntax-w">            </span><span class="devsite-syntax-p">},</span>
<span class="devsite-syntax-w">      </span><span class="devsite-syntax-p">},</span>
<span class="devsite-syntax-w">   </span><span class="devsite-syntax-p">});</span>

<span class="devsite-syntax-w">   </span><span class="devsite-syntax-kd">const</span><span class="devsite-syntax-w"> </span><span class="devsite-syntax-nx">data</span><span class="devsite-syntax-w"> </span><span class="devsite-syntax-o">=</span><span class="devsite-syntax-w"> </span><span class="devsite-syntax-nx">response</span><span class="devsite-syntax-p">.</span><span class="devsite-syntax-nx">candidates</span><span class="devsite-syntax-o">?</span><span class="devsite-syntax-p">.[</span><span class="devsite-syntax-mf">0</span><span class="devsite-syntax-p">]</span><span class="devsite-syntax-o">?</span><span class="devsite-syntax-p">.</span><span class="devsite-syntax-nx">content</span><span class="devsite-syntax-o">?</span><span class="devsite-syntax-p">.</span><span class="devsite-syntax-nx">parts</span><span class="devsite-syntax-o">?</span><span class="devsite-syntax-p">.[</span><span class="devsite-syntax-mf">0</span><span class="devsite-syntax-p">]</span><span class="devsite-syntax-o">?</span><span class="devsite-syntax-p">.</span><span class="devsite-syntax-nx">inlineData</span><span class="devsite-syntax-o">?</span><span class="devsite-syntax-p">.</span><span class="devsite-syntax-nx">data</span><span class="devsite-syntax-p">;</span>
<span class="devsite-syntax-w">   </span><span class="devsite-syntax-kd">const</span><span class="devsite-syntax-w"> </span><span class="devsite-syntax-nx">audioBuffer</span><span class="devsite-syntax-w"> </span><span class="devsite-syntax-o">=</span><span class="devsite-syntax-w"> </span><span class="devsite-syntax-nx">Buffer</span><span class="devsite-syntax-p">.</span><span class="devsite-syntax-kr">from</span><span class="devsite-syntax-p">(</span><span class="devsite-syntax-nx">data</span><span class="devsite-syntax-p">,</span><span class="devsite-syntax-w"> </span><span class="devsite-syntax-s1">'base64'</span><span class="devsite-syntax-p">);</span>

<span class="devsite-syntax-w">   </span><span class="devsite-syntax-kd">const</span><span class="devsite-syntax-w"> </span><span class="devsite-syntax-nx">fileName</span><span class="devsite-syntax-w"> </span><span class="devsite-syntax-o">=</span><span class="devsite-syntax-w"> </span><span class="devsite-syntax-s1">'out.wav'</span><span class="devsite-syntax-p">;</span>
<span class="devsite-syntax-w">   </span><span class="devsite-syntax-k">await</span><span class="devsite-syntax-w"> </span><span class="devsite-syntax-nx">saveWaveFile</span><span class="devsite-syntax-p">(</span><span class="devsite-syntax-nx">fileName</span><span class="devsite-syntax-p">,</span><span class="devsite-syntax-w"> </span><span class="devsite-syntax-nx">audioBuffer</span><span class="devsite-syntax-p">);</span>
<span class="devsite-syntax-p">}</span>
<span class="devsite-syntax-k">await</span><span class="devsite-syntax-w"> </span><span class="devsite-syntax-nx">main</span><span class="devsite-syntax-p">();</span>
</code></pre></devsite-code></section>
<section><h3 id="rest" data-text="REST" tabindex="-1">REST</h3><div></div><devsite-code><pre class="devsite-click-to-copy" translate="no" dir="ltr" is-upgraded syntax="Bash"><code translate="no" dir="ltr">curl<span class="devsite-syntax-w"> </span><span class="devsite-syntax-s2">"https://generativelanguage.googleapis.com/v1beta/models/gemini-3.1-flash-tts-preview:generateContent"</span><span class="devsite-syntax-w"> </span><span class="devsite-syntax-se">\</span>
<span class="devsite-syntax-w">  </span>-H<span class="devsite-syntax-w"> </span><span class="devsite-syntax-s2">"x-goog-api-key: </span><span class="devsite-syntax-nv">$GEMINI_API_KEY</span><span class="devsite-syntax-s2">"</span><span class="devsite-syntax-w"> </span><span class="devsite-syntax-se">\</span>
<span class="devsite-syntax-w">  </span>-X<span class="devsite-syntax-w"> </span>POST<span class="devsite-syntax-w"> </span><span class="devsite-syntax-se">\</span>
<span class="devsite-syntax-w">  </span>-H<span class="devsite-syntax-w"> </span><span class="devsite-syntax-s2">"Content-Type: application/json"</span><span class="devsite-syntax-w"> </span><span class="devsite-syntax-se">\</span>
<span class="devsite-syntax-w">  </span>-d<span class="devsite-syntax-w"> </span><span class="devsite-syntax-s1">'{</span>
<span class="devsite-syntax-s1">        "contents": [{</span>
<span class="devsite-syntax-s1">          "parts":[{</span>
<span class="devsite-syntax-s1">            "text": "Say cheerfully: Have a wonderful day!"</span>
<span class="devsite-syntax-s1">          }]</span>
<span class="devsite-syntax-s1">        }],</span>
<span class="devsite-syntax-s1">        "generationConfig": {</span>
<span class="devsite-syntax-s1">          "responseModalities": ["AUDIO"],</span>
<span class="devsite-syntax-s1">          "speechConfig": {</span>
<span class="devsite-syntax-s1">            "voiceConfig": {</span>
<span class="devsite-syntax-s1">              "prebuiltVoiceConfig": {</span>
<span class="devsite-syntax-s1">                "voiceName": "Kore"</span>
<span class="devsite-syntax-s1">              }</span>
<span class="devsite-syntax-s1">            }</span>
<span class="devsite-syntax-s1">          }</span>
<span class="devsite-syntax-s1">        },</span>
<span class="devsite-syntax-s1">        "model": "gemini-3.1-flash-tts-preview",</span>
<span class="devsite-syntax-s1">    }'</span><span class="devsite-syntax-w"> </span><span class="devsite-syntax-p">|</span><span class="devsite-syntax-w"> </span>jq<span class="devsite-syntax-w"> </span>-r<span class="devsite-syntax-w"> </span><span class="devsite-syntax-s1">'.candidates[0].content.parts[0].inlineData.data'</span><span class="devsite-syntax-w"> </span><span class="devsite-syntax-p">|</span><span class="devsite-syntax-w"> </span><span class="devsite-syntax-se">\</span>
<span class="devsite-syntax-w">          </span>base64<span class="devsite-syntax-w"> </span>--decode<span class="devsite-syntax-w"> </span>&gt;out.pcm
<span class="devsite-syntax-c1"># You may need to install ffmpeg.</span>
ffmpeg<span class="devsite-syntax-w"> </span>-f<span class="devsite-syntax-w"> </span>s16le<span class="devsite-syntax-w"> </span>-ar<span class="devsite-syntax-w"> </span><span class="devsite-syntax-m">24000</span><span class="devsite-syntax-w"> </span>-ac<span class="devsite-syntax-w"> </span><span class="devsite-syntax-m">1</span><span class="devsite-syntax-w"> </span>-i<span class="devsite-syntax-w"> </span>out.pcm<span class="devsite-syntax-w"> </span>out.wav
</code></pre></devsite-code></section>
</devsite-selector></div>
<h2 id="multi-speaker" data-text="Multi-speaker TTS" tabindex="-1">Multi-speaker TTS</h2>

<p>For multi-speaker audio, you&#39;ll need a <code translate="no" dir="ltr">MultiSpeakerVoiceConfig</code> object with
each speaker (up to 2) configured as a <code translate="no" dir="ltr">SpeakerVoiceConfig</code>.
You&#39;ll need to define each <code translate="no" dir="ltr">speaker</code> with the same names used in the
<a href="#controllable">prompt</a>:</p>
<div><devsite-selector data-ds-scope="code-sample">
<section><h3 id="python_1" data-text="Python" tabindex="-1">Python</h3><div></div><devsite-code><pre class="devsite-click-to-copy" translate="no" dir="ltr" is-upgraded syntax="Python"><code translate="no" dir="ltr"><span class="devsite-syntax-kn">from</span><span class="devsite-syntax-w"> </span><span class="devsite-syntax-nn">google</span><span class="devsite-syntax-w"> </span><span class="devsite-syntax-kn">import</span> <span class="devsite-syntax-n">genai</span>
<span class="devsite-syntax-kn">from</span><span class="devsite-syntax-w"> </span><span class="devsite-syntax-nn">google.genai</span><span class="devsite-syntax-w"> </span><span class="devsite-syntax-kn">import</span> <span class="devsite-syntax-n">types</span>
<span class="devsite-syntax-kn">import</span><span class="devsite-syntax-w"> </span><span class="devsite-syntax-nn">wave</span>

<span class="devsite-syntax-c1"># Set up the wave file to save the output:</span>
<span class="devsite-syntax-k">def</span><span class="devsite-syntax-w"> </span><span class="devsite-syntax-nf">wave_file</span><span class="devsite-syntax-p">(</span><span class="devsite-syntax-n">filename</span><span class="devsite-syntax-p">,</span> <span class="devsite-syntax-n">pcm</span><span class="devsite-syntax-p">,</span> <span class="devsite-syntax-n">channels</span><span class="devsite-syntax-o">=</span><span class="devsite-syntax-mi">1</span><span class="devsite-syntax-p">,</span> <span class="devsite-syntax-n">rate</span><span class="devsite-syntax-o">=</span><span class="devsite-syntax-mi">24000</span><span class="devsite-syntax-p">,</span> <span class="devsite-syntax-n">sample_width</span><span class="devsite-syntax-o">=</span><span class="devsite-syntax-mi">2</span><span class="devsite-syntax-p">):</span>
   <span class="devsite-syntax-k">with</span> <span class="devsite-syntax-n">wave</span><span class="devsite-syntax-o">.</span><span class="devsite-syntax-n">open</span><span class="devsite-syntax-p">(</span><span class="devsite-syntax-n">filename</span><span class="devsite-syntax-p">,</span> <span class="devsite-syntax-s2">"wb"</span><span class="devsite-syntax-p">)</span> <span class="devsite-syntax-k">as</span> <span class="devsite-syntax-n">wf</span><span class="devsite-syntax-p">:</span>
      <span class="devsite-syntax-n">wf</span><span class="devsite-syntax-o">.</span><span class="devsite-syntax-n">setnchannels</span><span class="devsite-syntax-p">(</span><span class="devsite-syntax-n">channels</span><span class="devsite-syntax-p">)</span>
      <span class="devsite-syntax-n">wf</span><span class="devsite-syntax-o">.</span><span class="devsite-syntax-n">setsampwidth</span><span class="devsite-syntax-p">(</span><span class="devsite-syntax-n">sample_width</span><span class="devsite-syntax-p">)</span>
      <span class="devsite-syntax-n">wf</span><span class="devsite-syntax-o">.</span><span class="devsite-syntax-n">setframerate</span><span class="devsite-syntax-p">(</span><span class="devsite-syntax-n">rate</span><span class="devsite-syntax-p">)</span>
      <span class="devsite-syntax-n">wf</span><span class="devsite-syntax-o">.</span><span class="devsite-syntax-n">writeframes</span><span class="devsite-syntax-p">(</span><span class="devsite-syntax-n">pcm</span><span class="devsite-syntax-p">)</span>

<span class="devsite-syntax-n">client</span> <span class="devsite-syntax-o">=</span> <span class="devsite-syntax-n">genai</span><span class="devsite-syntax-o">.</span><span class="devsite-syntax-n">Client</span><span class="devsite-syntax-p">()</span>

<span class="devsite-syntax-n">prompt</span> <span class="devsite-syntax-o">=</span> <span class="devsite-syntax-s2">"""TTS the following conversation between Joe and Jane:</span>
<span class="devsite-syntax-s2">         Joe: How's it going today Jane?</span>
<span class="devsite-syntax-s2">         Jane: Not too bad, how about you?"""</span>

<span class="devsite-syntax-n">response</span> <span class="devsite-syntax-o">=</span> <span class="devsite-syntax-n">client</span><span class="devsite-syntax-o">.</span><span class="devsite-syntax-n">models</span><span class="devsite-syntax-o">.</span><span class="devsite-syntax-n">generate_content</span><span class="devsite-syntax-p">(</span>
   <span class="devsite-syntax-n">model</span><span class="devsite-syntax-o">=</span><span class="devsite-syntax-s2">"gemini-3.1-flash-tts-preview"</span><span class="devsite-syntax-p">,</span>
   <span class="devsite-syntax-n">contents</span><span class="devsite-syntax-o">=</span><span class="devsite-syntax-n">prompt</span><span class="devsite-syntax-p">,</span>
   <span class="devsite-syntax-n">config</span><span class="devsite-syntax-o">=</span><span class="devsite-syntax-n">types</span><span class="devsite-syntax-o">.</span><span class="devsite-syntax-n">GenerateContentConfig</span><span class="devsite-syntax-p">(</span>
      <span class="devsite-syntax-n">response_modalities</span><span class="devsite-syntax-o">=</span><span class="devsite-syntax-p">[</span><span class="devsite-syntax-s2">"AUDIO"</span><span class="devsite-syntax-p">],</span>
      <span class="devsite-syntax-n">speech_config</span><span class="devsite-syntax-o">=</span><span class="devsite-syntax-n">types</span><span class="devsite-syntax-o">.</span><span class="devsite-syntax-n">SpeechConfig</span><span class="devsite-syntax-p">(</span>
         <span class="devsite-syntax-n">multi_speaker_voice_config</span><span class="devsite-syntax-o">=</span><span class="devsite-syntax-n">types</span><span class="devsite-syntax-o">.</span><span class="devsite-syntax-n">MultiSpeakerVoiceConfig</span><span class="devsite-syntax-p">(</span>
            <span class="devsite-syntax-n">speaker_voice_configs</span><span class="devsite-syntax-o">=</span><span class="devsite-syntax-p">[</span>
               <span class="devsite-syntax-n">types</span><span class="devsite-syntax-o">.</span><span class="devsite-syntax-n">SpeakerVoiceConfig</span><span class="devsite-syntax-p">(</span>
                  <span class="devsite-syntax-n">speaker</span><span class="devsite-syntax-o">=</span><span class="devsite-syntax-s1">'Joe'</span><span class="devsite-syntax-p">,</span>
                  <span class="devsite-syntax-n">voice_config</span><span class="devsite-syntax-o">=</span><span class="devsite-syntax-n">types</span><span class="devsite-syntax-o">.</span><span class="devsite-syntax-n">VoiceConfig</span><span class="devsite-syntax-p">(</span>
                     <span class="devsite-syntax-n">prebuilt_voice_config</span><span class="devsite-syntax-o">=</span><span class="devsite-syntax-n">types</span><span class="devsite-syntax-o">.</span><span class="devsite-syntax-n">PrebuiltVoiceConfig</span><span class="devsite-syntax-p">(</span>
                        <span class="devsite-syntax-n">voice_name</span><span class="devsite-syntax-o">=</span><span class="devsite-syntax-s1">'Kore'</span><span class="devsite-syntax-p">,</span>
                     <span class="devsite-syntax-p">)</span>
                  <span class="devsite-syntax-p">)</span>
               <span class="devsite-syntax-p">),</span>
               <span class="devsite-syntax-n">types</span><span class="devsite-syntax-o">.</span><span class="devsite-syntax-n">SpeakerVoiceConfig</span><span class="devsite-syntax-p">(</span>
                  <span class="devsite-syntax-n">speaker</span><span class="devsite-syntax-o">=</span><span class="devsite-syntax-s1">'Jane'</span><span class="devsite-syntax-p">,</span>
                  <span class="devsite-syntax-n">voice_config</span><span class="devsite-syntax-o">=</span><span class="devsite-syntax-n">types</span><span class="devsite-syntax-o">.</span><span class="devsite-syntax-n">VoiceConfig</span><span class="devsite-syntax-p">(</span>
                     <span class="devsite-syntax-n">prebuilt_voice_config</span><span class="devsite-syntax-o">=</span><span class="devsite-syntax-n">types</span><span class="devsite-syntax-o">.</span><span class="devsite-syntax-n">PrebuiltVoiceConfig</span><span class="devsite-syntax-p">(</span>
                        <span class="devsite-syntax-n">voice_name</span><span class="devsite-syntax-o">=</span><span class="devsite-syntax-s1">'Puck'</span><span class="devsite-syntax-p">,</span>
                     <span class="devsite-syntax-p">)</span>
                  <span class="devsite-syntax-p">)</span>
               <span class="devsite-syntax-p">),</span>
            <span class="devsite-syntax-p">]</span>
         <span class="devsite-syntax-p">)</span>
      <span class="devsite-syntax-p">)</span>
   <span class="devsite-syntax-p">)</span>
<span class="devsite-syntax-p">)</span>

<span class="devsite-syntax-n">data</span> <span class="devsite-syntax-o">=</span> <span class="devsite-syntax-n">response</span><span class="devsite-syntax-o">.</span><span class="devsite-syntax-n">candidates</span><span class="devsite-syntax-p">[</span><span class="devsite-syntax-mi">0</span><span class="devsite-syntax-p">]</span><span class="devsite-syntax-o">.</span><span class="devsite-syntax-n">content</span><span class="devsite-syntax-o">.</span><span class="devsite-syntax-n">parts</span><span class="devsite-syntax-p">[</span><span class="devsite-syntax-mi">0</span><span class="devsite-syntax-p">]</span><span class="devsite-syntax-o">.</span><span class="devsite-syntax-n">inline_data</span><span class="devsite-syntax-o">.</span><span class="devsite-syntax-n">data</span>

<span class="devsite-syntax-n">file_name</span><span class="devsite-syntax-o">=</span><span class="devsite-syntax-s1">'out.wav'</span>
<span class="devsite-syntax-n">wave_file</span><span class="devsite-syntax-p">(</span><span class="devsite-syntax-n">file_name</span><span class="devsite-syntax-p">,</span> <span class="devsite-syntax-n">data</span><span class="devsite-syntax-p">)</span> <span class="devsite-syntax-c1"># Saves the file to current directory</span>
</code></pre></devsite-code></section>
<section><h3 id="javascript_1" data-text="JavaScript" tabindex="-1">JavaScript</h3><div></div><devsite-code><pre class="devsite-click-to-copy" translate="no" dir="ltr" is-upgraded syntax="JavaScript"><code translate="no" dir="ltr"><span class="devsite-syntax-k">import</span><span class="devsite-syntax-w"> </span><span class="devsite-syntax-p">{</span><span class="devsite-syntax-nx">GoogleGenAI</span><span class="devsite-syntax-p">}</span><span class="devsite-syntax-w"> </span><span class="devsite-syntax-kr">from</span><span class="devsite-syntax-w"> </span><span class="devsite-syntax-s1">'@google/genai'</span><span class="devsite-syntax-p">;</span>
<span class="devsite-syntax-k">import</span><span class="devsite-syntax-w"> </span><span class="devsite-syntax-nx">wav</span><span class="devsite-syntax-w"> </span><span class="devsite-syntax-kr">from</span><span class="devsite-syntax-w"> </span><span class="devsite-syntax-s1">'wav'</span><span class="devsite-syntax-p">;</span>

<span class="devsite-syntax-k">async</span><span class="devsite-syntax-w"> </span><span class="devsite-syntax-kd">function</span><span class="devsite-syntax-w"> </span><span class="devsite-syntax-nx">saveWaveFile</span><span class="devsite-syntax-p">(</span>
<span class="devsite-syntax-w">   </span><span class="devsite-syntax-nx">filename</span><span class="devsite-syntax-p">,</span>
<span class="devsite-syntax-w">   </span><span class="devsite-syntax-nx">pcmData</span><span class="devsite-syntax-p">,</span>
<span class="devsite-syntax-w">   </span><span class="devsite-syntax-nx">channels</span><span class="devsite-syntax-w"> </span><span class="devsite-syntax-o">=</span><span class="devsite-syntax-w"> </span><span class="devsite-syntax-mf">1</span><span class="devsite-syntax-p">,</span>
<span class="devsite-syntax-w">   </span><span class="devsite-syntax-nx">rate</span><span class="devsite-syntax-w"> </span><span class="devsite-syntax-o">=</span><span class="devsite-syntax-w"> </span><span class="devsite-syntax-mf">24000</span><span class="devsite-syntax-p">,</span>
<span class="devsite-syntax-w">   </span><span class="devsite-syntax-nx">sampleWidth</span><span class="devsite-syntax-w"> </span><span class="devsite-syntax-o">=</span><span class="devsite-syntax-w"> </span><span class="devsite-syntax-mf">2</span><span class="devsite-syntax-p">,</span>
<span class="devsite-syntax-p">)</span><span class="devsite-syntax-w"> </span><span class="devsite-syntax-p">{</span>
<span class="devsite-syntax-w">   </span><span class="devsite-syntax-k">return</span><span class="devsite-syntax-w"> </span><span class="devsite-syntax-ow">new</span><span class="devsite-syntax-w"> </span><span class="devsite-syntax-nb">Promise</span><span class="devsite-syntax-p">((</span><span class="devsite-syntax-nx">resolve</span><span class="devsite-syntax-p">,</span><span class="devsite-syntax-w"> </span><span class="devsite-syntax-nx">reject</span><span class="devsite-syntax-p">)</span><span class="devsite-syntax-w"> </span><span class="devsite-syntax-o">=</span>&gt;<span class="devsite-syntax-w"> </span><span class="devsite-syntax-p">{</span>
<span class="devsite-syntax-w">      </span><span class="devsite-syntax-kd">const</span><span class="devsite-syntax-w"> </span><span class="devsite-syntax-nx">writer</span><span class="devsite-syntax-w"> </span><span class="devsite-syntax-o">=</span><span class="devsite-syntax-w"> </span><span class="devsite-syntax-ow">new</span><span class="devsite-syntax-w"> </span><span class="devsite-syntax-nx">wav</span><span class="devsite-syntax-p">.</span><span class="devsite-syntax-nx">FileWriter</span><span class="devsite-syntax-p">(</span><span class="devsite-syntax-nx">filename</span><span class="devsite-syntax-p">,</span><span class="devsite-syntax-w"> </span><span class="devsite-syntax-p">{</span>
<span class="devsite-syntax-w">            </span><span class="devsite-syntax-nx">channels</span><span class="devsite-syntax-p">,</span>
<span class="devsite-syntax-w">            </span><span class="devsite-syntax-nx">sampleRate</span><span class="devsite-syntax-o">:</span><span class="devsite-syntax-w"> </span><span class="devsite-syntax-nx">rate</span><span class="devsite-syntax-p">,</span>
<span class="devsite-syntax-w">            </span><span class="devsite-syntax-nx">bitDepth</span><span class="devsite-syntax-o">:</span><span class="devsite-syntax-w"> </span><span class="devsite-syntax-nx">sampleWidth</span><span class="devsite-syntax-w"> </span><span class="devsite-syntax-o">*</span><span class="devsite-syntax-w"> </span><span class="devsite-syntax-mf">8</span><span class="devsite-syntax-p">,</span>
<span class="devsite-syntax-w">      </span><span class="devsite-syntax-p">});</span>

<span class="devsite-syntax-w">      </span><span class="devsite-syntax-nx">writer</span><span class="devsite-syntax-p">.</span><span class="devsite-syntax-nx">on</span><span class="devsite-syntax-p">(</span><span class="devsite-syntax-s1">'finish'</span><span class="devsite-syntax-p">,</span><span class="devsite-syntax-w"> </span><span class="devsite-syntax-nx">resolve</span><span class="devsite-syntax-p">);</span>
<span class="devsite-syntax-w">      </span><span class="devsite-syntax-nx">writer</span><span class="devsite-syntax-p">.</span><span class="devsite-syntax-nx">on</span><span class="devsite-syntax-p">(</span><span class="devsite-syntax-s1">'error'</span><span class="devsite-syntax-p">,</span><span class="devsite-syntax-w"> </span><span class="devsite-syntax-nx">reject</span><span class="devsite-syntax-p">);</span>

<span class="devsite-syntax-w">      </span><span class="devsite-syntax-nx">writer</span><span class="devsite-syntax-p">.</span><span class="devsite-syntax-nx">write</span><span class="devsite-syntax-p">(</span><span class="devsite-syntax-nx">pcmData</span><span class="devsite-syntax-p">);</span>
<span class="devsite-syntax-w">      </span><span class="devsite-syntax-nx">writer</span><span class="devsite-syntax-p">.</span><span class="devsite-syntax-nx">end</span><span class="devsite-syntax-p">();</span>
<span class="devsite-syntax-w">   </span><span class="devsite-syntax-p">});</span>
<span class="devsite-syntax-p">}</span>

<span class="devsite-syntax-k">async</span><span class="devsite-syntax-w"> </span><span class="devsite-syntax-kd">function</span><span class="devsite-syntax-w"> </span><span class="devsite-syntax-nx">main</span><span class="devsite-syntax-p">()</span><span class="devsite-syntax-w"> </span><span class="devsite-syntax-p">{</span>
<span class="devsite-syntax-w">   </span><span class="devsite-syntax-kd">const</span><span class="devsite-syntax-w"> </span><span class="devsite-syntax-nx">ai</span><span class="devsite-syntax-w"> </span><span class="devsite-syntax-o">=</span><span class="devsite-syntax-w"> </span><span class="devsite-syntax-ow">new</span><span class="devsite-syntax-w"> </span><span class="devsite-syntax-nx">GoogleGenAI</span><span class="devsite-syntax-p">({});</span>

<span class="devsite-syntax-w">   </span><span class="devsite-syntax-kd">const</span><span class="devsite-syntax-w"> </span><span class="devsite-syntax-nx">prompt</span><span class="devsite-syntax-w"> </span><span class="devsite-syntax-o">=</span><span class="devsite-syntax-w"> </span><span class="devsite-syntax-sb">`TTS the following conversation between Joe and Jane:</span>
<span class="devsite-syntax-sb">         Joe: How's it going today Jane?</span>
<span class="devsite-syntax-sb">         Jane: Not too bad, how about you?`</span><span class="devsite-syntax-p">;</span>

<span class="devsite-syntax-w">   </span><span class="devsite-syntax-kd">const</span><span class="devsite-syntax-w"> </span><span class="devsite-syntax-nx">response</span><span class="devsite-syntax-w"> </span><span class="devsite-syntax-o">=</span><span class="devsite-syntax-w"> </span><span class="devsite-syntax-k">await</span><span class="devsite-syntax-w"> </span><span class="devsite-syntax-nx">ai</span><span class="devsite-syntax-p">.</span><span class="devsite-syntax-nx">models</span><span class="devsite-syntax-p">.</span><span class="devsite-syntax-nx">generateContent</span><span class="devsite-syntax-p">({</span>
<span class="devsite-syntax-w">      </span><span class="devsite-syntax-nx">model</span><span class="devsite-syntax-o">:</span><span class="devsite-syntax-w"> </span><span class="devsite-syntax-s2">"gemini-3.1-flash-tts-preview"</span><span class="devsite-syntax-p">,</span>
<span class="devsite-syntax-w">      </span><span class="devsite-syntax-nx">contents</span><span class="devsite-syntax-o">:</span><span class="devsite-syntax-w"> </span><span class="devsite-syntax-p">[{</span><span class="devsite-syntax-w"> </span><span class="devsite-syntax-nx">parts</span><span class="devsite-syntax-o">:</span><span class="devsite-syntax-w"> </span><span class="devsite-syntax-p">[{</span><span class="devsite-syntax-w"> </span><span class="devsite-syntax-nx">text</span><span class="devsite-syntax-o">:</span><span class="devsite-syntax-w"> </span><span class="devsite-syntax-nx">prompt</span><span class="devsite-syntax-w"> </span><span class="devsite-syntax-p">}]</span><span class="devsite-syntax-w"> </span><span class="devsite-syntax-p">}],</span>
<span class="devsite-syntax-w">      </span><span class="devsite-syntax-nx">config</span><span class="devsite-syntax-o">:</span><span class="devsite-syntax-w"> </span><span class="devsite-syntax-p">{</span>
<span class="devsite-syntax-w">            </span><span class="devsite-syntax-nx">responseModalities</span><span class="devsite-syntax-o">:</span><span class="devsite-syntax-w"> </span><span class="devsite-syntax-p">[</span><span class="devsite-syntax-s1">'AUDIO'</span><span class="devsite-syntax-p">],</span>
<span class="devsite-syntax-w">            </span><span class="devsite-syntax-nx">speechConfig</span><span class="devsite-syntax-o">:</span><span class="devsite-syntax-w"> </span><span class="devsite-syntax-p">{</span>
<span class="devsite-syntax-w">               </span><span class="devsite-syntax-nx">multiSpeakerVoiceConfig</span><span class="devsite-syntax-o">:</span><span class="devsite-syntax-w"> </span><span class="devsite-syntax-p">{</span>
<span class="devsite-syntax-w">                  </span><span class="devsite-syntax-nx">speakerVoiceConfigs</span><span class="devsite-syntax-o">:</span><span class="devsite-syntax-w"> </span><span class="devsite-syntax-p">[</span>
<span class="devsite-syntax-w">                        </span><span class="devsite-syntax-p">{</span>
<span class="devsite-syntax-w">                           </span><span class="devsite-syntax-nx">speaker</span><span class="devsite-syntax-o">:</span><span class="devsite-syntax-w"> </span><span class="devsite-syntax-s1">'Joe'</span><span class="devsite-syntax-p">,</span>
<span class="devsite-syntax-w">                           </span><span class="devsite-syntax-nx">voiceConfig</span><span class="devsite-syntax-o">:</span><span class="devsite-syntax-w"> </span><span class="devsite-syntax-p">{</span>
<span class="devsite-syntax-w">                              </span><span class="devsite-syntax-nx">prebuiltVoiceConfig</span><span class="devsite-syntax-o">:</span><span class="devsite-syntax-w"> </span><span class="devsite-syntax-p">{</span><span class="devsite-syntax-w"> </span><span class="devsite-syntax-nx">voiceName</span><span class="devsite-syntax-o">:</span><span class="devsite-syntax-w"> </span><span class="devsite-syntax-s1">'Kore'</span><span class="devsite-syntax-w"> </span><span class="devsite-syntax-p">}</span>
<span class="devsite-syntax-w">                           </span><span class="devsite-syntax-p">}</span>
<span class="devsite-syntax-w">                        </span><span class="devsite-syntax-p">},</span>
<span class="devsite-syntax-w">                        </span><span class="devsite-syntax-p">{</span>
<span class="devsite-syntax-w">                           </span><span class="devsite-syntax-nx">speaker</span><span class="devsite-syntax-o">:</span><span class="devsite-syntax-w"> </span><span class="devsite-syntax-s1">'Jane'</span><span class="devsite-syntax-p">,</span>
<span class="devsite-syntax-w">                           </span><span class="devsite-syntax-nx">voiceConfig</span><span class="devsite-syntax-o">:</span><span class="devsite-syntax-w"> </span><span class="devsite-syntax-p">{</span>
<span class="devsite-syntax-w">                              </span><span class="devsite-syntax-nx">prebuiltVoiceConfig</span><span class="devsite-syntax-o">:</span><span class="devsite-syntax-w"> </span><span class="devsite-syntax-p">{</span><span class="devsite-syntax-w"> </span><span class="devsite-syntax-nx">voiceName</span><span class="devsite-syntax-o">:</span><span class="devsite-syntax-w"> </span><span class="devsite-syntax-s1">'Puck'</span><span class="devsite-syntax-w"> </span><span class="devsite-syntax-p">}</span>
<span class="devsite-syntax-w">                           </span><span class="devsite-syntax-p">}</span>
<span class="devsite-syntax-w">                        </span><span class="devsite-syntax-p">}</span>
<span class="devsite-syntax-w">                  </span><span class="devsite-syntax-p">]</span>
<span class="devsite-syntax-w">               </span><span class="devsite-syntax-p">}</span>
<span class="devsite-syntax-w">            </span><span class="devsite-syntax-p">}</span>
<span class="devsite-syntax-w">      </span><span class="devsite-syntax-p">}</span>
<span class="devsite-syntax-w">   </span><span class="devsite-syntax-p">});</span>

<span class="devsite-syntax-w">   </span><span class="devsite-syntax-kd">const</span><span class="devsite-syntax-w"> </span><span class="devsite-syntax-nx">data</span><span class="devsite-syntax-w"> </span><span class="devsite-syntax-o">=</span><span class="devsite-syntax-w"> </span><span class="devsite-syntax-nx">response</span><span class="devsite-syntax-p">.</span><span class="devsite-syntax-nx">candidates</span><span class="devsite-syntax-o">?</span><span class="devsite-syntax-p">.[</span><span class="devsite-syntax-mf">0</span><span class="devsite-syntax-p">]</span><span class="devsite-syntax-o">?</span><span class="devsite-syntax-p">.</span><span class="devsite-syntax-nx">content</span><span class="devsite-syntax-o">?</span><span class="devsite-syntax-p">.</span><span class="devsite-syntax-nx">parts</span><span class="devsite-syntax-o">?</span><span class="devsite-syntax-p">.[</span><span class="devsite-syntax-mf">0</span><span class="devsite-syntax-p">]</span><span class="devsite-syntax-o">?</span><span class="devsite-syntax-p">.</span><span class="devsite-syntax-nx">inlineData</span><span class="devsite-syntax-o">?</span><span class="devsite-syntax-p">.</span><span class="devsite-syntax-nx">data</span><span class="devsite-syntax-p">;</span>
<span class="devsite-syntax-w">   </span><span class="devsite-syntax-kd">const</span><span class="devsite-syntax-w"> </span><span class="devsite-syntax-nx">audioBuffer</span><span class="devsite-syntax-w"> </span><span class="devsite-syntax-o">=</span><span class="devsite-syntax-w"> </span><span class="devsite-syntax-nx">Buffer</span><span class="devsite-syntax-p">.</span><span class="devsite-syntax-kr">from</span><span class="devsite-syntax-p">(</span><span class="devsite-syntax-nx">data</span><span class="devsite-syntax-p">,</span><span class="devsite-syntax-w"> </span><span class="devsite-syntax-s1">'base64'</span><span class="devsite-syntax-p">);</span>

<span class="devsite-syntax-w">   </span><span class="devsite-syntax-kd">const</span><span class="devsite-syntax-w"> </span><span class="devsite-syntax-nx">fileName</span><span class="devsite-syntax-w"> </span><span class="devsite-syntax-o">=</span><span class="devsite-syntax-w"> </span><span class="devsite-syntax-s1">'out.wav'</span><span class="devsite-syntax-p">;</span>
<span class="devsite-syntax-w">   </span><span class="devsite-syntax-k">await</span><span class="devsite-syntax-w"> </span><span class="devsite-syntax-nx">saveWaveFile</span><span class="devsite-syntax-p">(</span><span class="devsite-syntax-nx">fileName</span><span class="devsite-syntax-p">,</span><span class="devsite-syntax-w"> </span><span class="devsite-syntax-nx">audioBuffer</span><span class="devsite-syntax-p">);</span>
<span class="devsite-syntax-p">}</span>

<span class="devsite-syntax-k">await</span><span class="devsite-syntax-w"> </span><span class="devsite-syntax-nx">main</span><span class="devsite-syntax-p">();</span>
</code></pre></devsite-code></section>
<section><h3 id="rest_1" data-text="REST" tabindex="-1">REST</h3><div></div><devsite-code><pre class="devsite-click-to-copy" translate="no" dir="ltr" is-upgraded syntax="Bash"><code translate="no" dir="ltr">curl<span class="devsite-syntax-w"> </span><span class="devsite-syntax-s2">"https://generativelanguage.googleapis.com/v1beta/models/gemini-3.1-flash-tts-preview:generateContent"</span><span class="devsite-syntax-w"> </span><span class="devsite-syntax-se">\</span>
<span class="devsite-syntax-w">  </span>-H<span class="devsite-syntax-w"> </span><span class="devsite-syntax-s2">"x-goog-api-key: </span><span class="devsite-syntax-nv">$GEMINI_API_KEY</span><span class="devsite-syntax-s2">"</span><span class="devsite-syntax-w"> </span><span class="devsite-syntax-se">\</span>
<span class="devsite-syntax-w">  </span>-X<span class="devsite-syntax-w"> </span>POST<span class="devsite-syntax-w"> </span><span class="devsite-syntax-se">\</span>
<span class="devsite-syntax-w">  </span>-H<span class="devsite-syntax-w"> </span><span class="devsite-syntax-s2">"Content-Type: application/json"</span><span class="devsite-syntax-w"> </span><span class="devsite-syntax-se">\</span>
<span class="devsite-syntax-w">  </span>-d<span class="devsite-syntax-w"> </span><span class="devsite-syntax-s1">'{</span>
<span class="devsite-syntax-s1">  "contents": [{</span>
<span class="devsite-syntax-s1">    "parts":[{</span>
<span class="devsite-syntax-s1">      "text": "TTS the following conversation between Joe and Jane:</span>
<span class="devsite-syntax-s1">                Joe: Hows it going today Jane?</span>
<span class="devsite-syntax-s1">                Jane: Not too bad, how about you?"</span>
<span class="devsite-syntax-s1">    }]</span>
<span class="devsite-syntax-s1">  }],</span>
<span class="devsite-syntax-s1">  "generationConfig": {</span>
<span class="devsite-syntax-s1">    "responseModalities": ["AUDIO"],</span>
<span class="devsite-syntax-s1">    "speechConfig": {</span>
<span class="devsite-syntax-s1">      "multiSpeakerVoiceConfig": {</span>
<span class="devsite-syntax-s1">        "speakerVoiceConfigs": [{</span>
<span class="devsite-syntax-s1">            "speaker": "Joe",</span>
<span class="devsite-syntax-s1">            "voiceConfig": {</span>
<span class="devsite-syntax-s1">              "prebuiltVoiceConfig": {</span>
<span class="devsite-syntax-s1">                "voiceName": "Kore"</span>
<span class="devsite-syntax-s1">              }</span>
<span class="devsite-syntax-s1">            }</span>
<span class="devsite-syntax-s1">          }, {</span>
<span class="devsite-syntax-s1">            "speaker": "Jane",</span>
<span class="devsite-syntax-s1">            "voiceConfig": {</span>
<span class="devsite-syntax-s1">              "prebuiltVoiceConfig": {</span>
<span class="devsite-syntax-s1">                "voiceName": "Puck"</span>
<span class="devsite-syntax-s1">              }</span>
<span class="devsite-syntax-s1">            }</span>
<span class="devsite-syntax-s1">          }]</span>
<span class="devsite-syntax-s1">      }</span>
<span class="devsite-syntax-s1">    }</span>
<span class="devsite-syntax-s1">  },</span>
<span class="devsite-syntax-s1">  "model": "gemini-3.1-flash-tts-preview",</span>
<span class="devsite-syntax-s1">}'</span><span class="devsite-syntax-w"> </span><span class="devsite-syntax-p">|</span><span class="devsite-syntax-w"> </span>jq<span class="devsite-syntax-w"> </span>-r<span class="devsite-syntax-w"> </span><span class="devsite-syntax-s1">'.candidates[0].content.parts[0].inlineData.data'</span><span class="devsite-syntax-w"> </span><span class="devsite-syntax-p">|</span><span class="devsite-syntax-w"> </span><span class="devsite-syntax-se">\</span>
<span class="devsite-syntax-w">    </span>base64<span class="devsite-syntax-w"> </span>--decode<span class="devsite-syntax-w"> &gt; </span>out.pcm
<span class="devsite-syntax-c1"># You may need to install ffmpeg.</span>
ffmpeg<span class="devsite-syntax-w"> </span>-f<span class="devsite-syntax-w"> </span>s16le<span class="devsite-syntax-w"> </span>-ar<span class="devsite-syntax-w"> </span><span class="devsite-syntax-m">24000</span><span class="devsite-syntax-w"> </span>-ac<span class="devsite-syntax-w"> </span><span class="devsite-syntax-m">1</span><span class="devsite-syntax-w"> </span>-i<span class="devsite-syntax-w"> </span>out.pcm<span class="devsite-syntax-w"> </span>out.wav
</code></pre></devsite-code></section>
</devsite-selector></div>
<h2 id="controllable" data-text="Controlling speech style with prompts" tabindex="-1">Controlling speech style with prompts</h2>

<p>You can control style, tone, accent, and pace using natural language prompts
or <a href="#transcript-tags">audio tags</a> for both single- and multi-speaker TTS.
For example, in a single-speaker prompt, you can say:</p>
<div></div><devsite-code><pre class="devsite-click-to-copy" translate="no" dir="ltr" is-upgraded><code translate="no" dir="ltr">Say in an spooky voice:
&#34;By the pricking of my thumbs... [short pause]
[whisper] Something wicked this way comes&#34;
</code></pre></devsite-code>
<p>In a multi-speaker prompt, provide the model with each speaker&#39;s name and
corresponding transcript. You can also provide guidance for each speaker
individually:</p>
<div></div><devsite-code><pre class="devsite-click-to-copy" translate="no" dir="ltr" is-upgraded><code translate="no" dir="ltr">Make Speaker1 sound tired and bored, and Speaker2 sound excited and happy:

Speaker1: So... [yawn] what&#39;s on the agenda today?
Speaker2: You&#39;re never going to guess!
</code></pre></devsite-code>
<p>Try using a <a href="#voices">voice option</a> that corresponds to the style or emotion you
want to convey, to emphasize it even more. In the previous prompt, for example,
<em>Enceladus</em>&#39;s breathiness might emphasize &quot;tired&quot; and &quot;bored&quot;, while
<em>Puck</em>&#39;s upbeat tone could complement &quot;excited&quot; and &quot;happy&quot;.</p>
<aside class="tip"><strong>Tip:</strong><span> The <a href="https://aistudio.google.com/apps/bundled/voice-library?showPreview=true">Voice Library</a>
applet in Google AI Studio is a great way to try out speech styles and voices
with Gemini TTS.</span></aside>
<h2 id="prompt-tts" data-text="Generating a prompt to convert to audio" tabindex="-1">Generating a prompt to convert to audio</h2>

<p>The TTS models only output audio, but you can use
<a href="/gemini-api/docs/models">other models</a> to generate a transcript first,
then pass that transcript to the TTS model to read aloud.</p>
<div><devsite-selector data-ds-scope="code-sample">
<section><h3 id="python_2" data-text="Python" tabindex="-1">Python</h3><div></div><devsite-code><pre class="devsite-click-to-copy" translate="no" dir="ltr" is-upgraded syntax="Python"><code translate="no" dir="ltr"><span class="devsite-syntax-kn">from</span><span class="devsite-syntax-w"> </span><span class="devsite-syntax-nn">google</span><span class="devsite-syntax-w"> </span><span class="devsite-syntax-kn">import</span> <span class="devsite-syntax-n">genai</span>
<span class="devsite-syntax-kn">from</span><span class="devsite-syntax-w"> </span><span class="devsite-syntax-nn">google.genai</span><span class="devsite-syntax-w"> </span><span class="devsite-syntax-kn">import</span> <span class="devsite-syntax-n">types</span>

<span class="devsite-syntax-n">client</span> <span class="devsite-syntax-o">=</span> <span class="devsite-syntax-n">genai</span><span class="devsite-syntax-o">.</span><span class="devsite-syntax-n">Client</span><span class="devsite-syntax-p">()</span>

<span class="devsite-syntax-n">transcript</span> <span class="devsite-syntax-o">=</span> <span class="devsite-syntax-n">client</span><span class="devsite-syntax-o">.</span><span class="devsite-syntax-n">models</span><span class="devsite-syntax-o">.</span><span class="devsite-syntax-n">generate_content</span><span class="devsite-syntax-p">(</span>
   <span class="devsite-syntax-n">model</span><span class="devsite-syntax-o">=</span><span class="devsite-syntax-s2">"gemini-3.5-flash"</span><span class="devsite-syntax-p">,</span>
   <span class="devsite-syntax-n">contents</span><span class="devsite-syntax-o">=</span><span class="devsite-syntax-s2">"""Generate a short transcript around 100 words that reads</span>
<span class="devsite-syntax-s2">            like it was clipped from a podcast by excited herpetologists.</span>
<span class="devsite-syntax-s2">            The hosts names are Dr. Anya and Liam."""</span><span class="devsite-syntax-p">)</span><span class="devsite-syntax-o">.</span><span class="devsite-syntax-n">text</span>

<span class="devsite-syntax-n">response</span> <span class="devsite-syntax-o">=</span> <span class="devsite-syntax-n">client</span><span class="devsite-syntax-o">.</span><span class="devsite-syntax-n">models</span><span class="devsite-syntax-o">.</span><span class="devsite-syntax-n">generate_content</span><span class="devsite-syntax-p">(</span>
   <span class="devsite-syntax-n">model</span><span class="devsite-syntax-o">=</span><span class="devsite-syntax-s2">"gemini-3.1-flash-tts-preview"</span><span class="devsite-syntax-p">,</span>
   <span class="devsite-syntax-n">contents</span><span class="devsite-syntax-o">=</span><span class="devsite-syntax-n">transcript</span><span class="devsite-syntax-p">,</span>
   <span class="devsite-syntax-n">config</span><span class="devsite-syntax-o">=</span><span class="devsite-syntax-n">types</span><span class="devsite-syntax-o">.</span><span class="devsite-syntax-n">GenerateContentConfig</span><span class="devsite-syntax-p">(</span>
      <span class="devsite-syntax-n">response_modalities</span><span class="devsite-syntax-o">=</span><span class="devsite-syntax-p">[</span><span class="devsite-syntax-s2">"AUDIO"</span><span class="devsite-syntax-p">],</span>
      <span class="devsite-syntax-n">speech_config</span><span class="devsite-syntax-o">=</span><span class="devsite-syntax-n">types</span><span class="devsite-syntax-o">.</span><span class="devsite-syntax-n">SpeechConfig</span><span class="devsite-syntax-p">(</span>
         <span class="devsite-syntax-n">multi_speaker_voice_config</span><span class="devsite-syntax-o">=</span><span class="devsite-syntax-n">types</span><span class="devsite-syntax-o">.</span><span class="devsite-syntax-n">MultiSpeakerVoiceConfig</span><span class="devsite-syntax-p">(</span>
            <span class="devsite-syntax-n">speaker_voice_configs</span><span class="devsite-syntax-o">=</span><span class="devsite-syntax-p">[</span>
               <span class="devsite-syntax-n">types</span><span class="devsite-syntax-o">.</span><span class="devsite-syntax-n">SpeakerVoiceConfig</span><span class="devsite-syntax-p">(</span>
                  <span class="devsite-syntax-n">speaker</span><span class="devsite-syntax-o">=</span><span class="devsite-syntax-s1">'Dr. Anya'</span><span class="devsite-syntax-p">,</span>
                  <span class="devsite-syntax-n">voice_config</span><span class="devsite-syntax-o">=</span><span class="devsite-syntax-n">types</span><span class="devsite-syntax-o">.</span><span class="devsite-syntax-n">VoiceConfig</span><span class="devsite-syntax-p">(</span>
                     <span class="devsite-syntax-n">prebuilt_voice_config</span><span class="devsite-syntax-o">=</span><span class="devsite-syntax-n">types</span><span class="devsite-syntax-o">.</span><span class="devsite-syntax-n">PrebuiltVoiceConfig</span><span class="devsite-syntax-p">(</span>
                        <span class="devsite-syntax-n">voice_name</span><span class="devsite-syntax-o">=</span><span class="devsite-syntax-s1">'Kore'</span><span class="devsite-syntax-p">,</span>
                     <span class="devsite-syntax-p">)</span>
                  <span class="devsite-syntax-p">)</span>
               <span class="devsite-syntax-p">),</span>
               <span class="devsite-syntax-n">types</span><span class="devsite-syntax-o">.</span><span class="devsite-syntax-n">SpeakerVoiceConfig</span><span class="devsite-syntax-p">(</span>
                  <span class="devsite-syntax-n">speaker</span><span class="devsite-syntax-o">=</span><span class="devsite-syntax-s1">'Liam'</span><span class="devsite-syntax-p">,</span>
                  <span class="devsite-syntax-n">voice_config</span><span class="devsite-syntax-o">=</span><span class="devsite-syntax-n">types</span><span class="devsite-syntax-o">.</span><span class="devsite-syntax-n">VoiceConfig</span><span class="devsite-syntax-p">(</span>
                     <span class="devsite-syntax-n">prebuilt_voice_config</span><span class="devsite-syntax-o">=</span><span class="devsite-syntax-n">types</span><span class="devsite-syntax-o">.</span><span class="devsite-syntax-n">PrebuiltVoiceConfig</span><span class="devsite-syntax-p">(</span>
                        <span class="devsite-syntax-n">voice_name</span><span class="devsite-syntax-o">=</span><span class="devsite-syntax-s1">'Puck'</span><span class="devsite-syntax-p">,</span>
                     <span class="devsite-syntax-p">)</span>
                  <span class="devsite-syntax-p">)</span>
               <span class="devsite-syntax-p">),</span>
            <span class="devsite-syntax-p">]</span>
         <span class="devsite-syntax-p">)</span>
      <span class="devsite-syntax-p">)</span>
   <span class="devsite-syntax-p">)</span>
<span class="devsite-syntax-p">)</span>

<span class="devsite-syntax-c1"># ...Code to handle audio output</span>
</code></pre></devsite-code></section>
<section><h3 id="javascript_2" data-text="JavaScript" tabindex="-1">JavaScript</h3><div></div><devsite-code><pre class="devsite-click-to-copy" translate="no" dir="ltr" is-upgraded syntax="JavaScript"><code translate="no" dir="ltr"><span class="devsite-syntax-k">import</span><span class="devsite-syntax-w"> </span><span class="devsite-syntax-p">{</span><span class="devsite-syntax-w"> </span><span class="devsite-syntax-nx">GoogleGenAI</span><span class="devsite-syntax-w"> </span><span class="devsite-syntax-p">}</span><span class="devsite-syntax-w"> </span><span class="devsite-syntax-kr">from</span><span class="devsite-syntax-w"> </span><span class="devsite-syntax-s2">"@google/genai"</span><span class="devsite-syntax-p">;</span>

<span class="devsite-syntax-kd">const</span><span class="devsite-syntax-w"> </span><span class="devsite-syntax-nx">ai</span><span class="devsite-syntax-w"> </span><span class="devsite-syntax-o">=</span><span class="devsite-syntax-w"> </span><span class="devsite-syntax-ow">new</span><span class="devsite-syntax-w"> </span><span class="devsite-syntax-nx">GoogleGenAI</span><span class="devsite-syntax-p">({});</span>

<span class="devsite-syntax-k">async</span><span class="devsite-syntax-w"> </span><span class="devsite-syntax-kd">function</span><span class="devsite-syntax-w"> </span><span class="devsite-syntax-nx">main</span><span class="devsite-syntax-p">()</span><span class="devsite-syntax-w"> </span><span class="devsite-syntax-p">{</span>

<span class="devsite-syntax-kd">const</span><span class="devsite-syntax-w"> </span><span class="devsite-syntax-nx">transcript</span><span class="devsite-syntax-w"> </span><span class="devsite-syntax-o">=</span><span class="devsite-syntax-w"> </span><span class="devsite-syntax-k">await</span><span class="devsite-syntax-w"> </span><span class="devsite-syntax-nx">ai</span><span class="devsite-syntax-p">.</span><span class="devsite-syntax-nx">models</span><span class="devsite-syntax-p">.</span><span class="devsite-syntax-nx">generateContent</span><span class="devsite-syntax-p">({</span>
<span class="devsite-syntax-w">   </span><span class="devsite-syntax-nx">model</span><span class="devsite-syntax-o">:</span><span class="devsite-syntax-w"> </span><span class="devsite-syntax-s2">"gemini-3.5-flash"</span><span class="devsite-syntax-p">,</span>
<span class="devsite-syntax-w">   </span><span class="devsite-syntax-nx">contents</span><span class="devsite-syntax-o">:</span><span class="devsite-syntax-w"> </span><span class="devsite-syntax-s2">"Generate a short transcript around 100 words that reads like it was clipped from a podcast by excited herpetologists. The hosts names are Dr. Anya and Liam."</span><span class="devsite-syntax-p">,</span>
<span class="devsite-syntax-w">   </span><span class="devsite-syntax-p">})</span>

<span class="devsite-syntax-kd">const</span><span class="devsite-syntax-w"> </span><span class="devsite-syntax-nx">response</span><span class="devsite-syntax-w"> </span><span class="devsite-syntax-o">=</span><span class="devsite-syntax-w"> </span><span class="devsite-syntax-k">await</span><span class="devsite-syntax-w"> </span><span class="devsite-syntax-nx">ai</span><span class="devsite-syntax-p">.</span><span class="devsite-syntax-nx">models</span><span class="devsite-syntax-p">.</span><span class="devsite-syntax-nx">generateContent</span><span class="devsite-syntax-p">({</span>
<span class="devsite-syntax-w">   </span><span class="devsite-syntax-nx">model</span><span class="devsite-syntax-o">:</span><span class="devsite-syntax-w"> </span><span class="devsite-syntax-s2">"gemini-3.1-flash-tts-preview"</span><span class="devsite-syntax-p">,</span>
<span class="devsite-syntax-w">   </span><span class="devsite-syntax-nx">contents</span><span class="devsite-syntax-o">:</span><span class="devsite-syntax-w"> </span><span class="devsite-syntax-nx">transcript</span><span class="devsite-syntax-p">,</span>
<span class="devsite-syntax-w">   </span><span class="devsite-syntax-nx">config</span><span class="devsite-syntax-o">:</span><span class="devsite-syntax-w"> </span><span class="devsite-syntax-p">{</span>
<span class="devsite-syntax-w">      </span><span class="devsite-syntax-nx">responseModalities</span><span class="devsite-syntax-o">:</span><span class="devsite-syntax-w"> </span><span class="devsite-syntax-p">[</span><span class="devsite-syntax-s1">'AUDIO'</span><span class="devsite-syntax-p">],</span>
<span class="devsite-syntax-w">      </span><span class="devsite-syntax-nx">speechConfig</span><span class="devsite-syntax-o">:</span><span class="devsite-syntax-w"> </span><span class="devsite-syntax-p">{</span>
<span class="devsite-syntax-w">         </span><span class="devsite-syntax-nx">multiSpeakerVoiceConfig</span><span class="devsite-syntax-o">:</span><span class="devsite-syntax-w"> </span><span class="devsite-syntax-p">{</span>
<span class="devsite-syntax-w">            </span><span class="devsite-syntax-nx">speakerVoiceConfigs</span><span class="devsite-syntax-o">:</span><span class="devsite-syntax-w"> </span><span class="devsite-syntax-p">[</span>
<span class="devsite-syntax-w">                   </span><span class="devsite-syntax-p">{</span>
<span class="devsite-syntax-w">                     </span><span class="devsite-syntax-nx">speaker</span><span class="devsite-syntax-o">:</span><span class="devsite-syntax-w"> </span><span class="devsite-syntax-s2">"Dr. Anya"</span><span class="devsite-syntax-p">,</span>
<span class="devsite-syntax-w">                     </span><span class="devsite-syntax-nx">voiceConfig</span><span class="devsite-syntax-o">:</span><span class="devsite-syntax-w"> </span><span class="devsite-syntax-p">{</span>
<span class="devsite-syntax-w">                        </span><span class="devsite-syntax-nx">prebuiltVoiceConfig</span><span class="devsite-syntax-o">:</span><span class="devsite-syntax-w"> </span><span class="devsite-syntax-p">{</span><span class="devsite-syntax-nx">voiceName</span><span class="devsite-syntax-o">:</span><span class="devsite-syntax-w"> </span><span class="devsite-syntax-s2">"Kore"</span><span class="devsite-syntax-p">},</span>
<span class="devsite-syntax-w">                     </span><span class="devsite-syntax-p">}</span>
<span class="devsite-syntax-w">                  </span><span class="devsite-syntax-p">},</span>
<span class="devsite-syntax-w">                  </span><span class="devsite-syntax-p">{</span>
<span class="devsite-syntax-w">                     </span><span class="devsite-syntax-nx">speaker</span><span class="devsite-syntax-o">:</span><span class="devsite-syntax-w"> </span><span class="devsite-syntax-s2">"Liam"</span><span class="devsite-syntax-p">,</span>
<span class="devsite-syntax-w">                     </span><span class="devsite-syntax-nx">voiceConfig</span><span class="devsite-syntax-o">:</span><span class="devsite-syntax-w"> </span><span class="devsite-syntax-p">{</span>
<span class="devsite-syntax-w">                        </span><span class="devsite-syntax-nx">prebuiltVoiceConfig</span><span class="devsite-syntax-o">:</span><span class="devsite-syntax-w"> </span><span class="devsite-syntax-p">{</span><span class="devsite-syntax-nx">voiceName</span><span class="devsite-syntax-o">:</span><span class="devsite-syntax-w"> </span><span class="devsite-syntax-s2">"Puck"</span><span class="devsite-syntax-p">},</span>
<span class="devsite-syntax-w">                    </span><span class="devsite-syntax-p">}</span>
<span class="devsite-syntax-w">                  </span><span class="devsite-syntax-p">}</span>
<span class="devsite-syntax-w">                </span><span class="devsite-syntax-p">]</span>
<span class="devsite-syntax-w">              </span><span class="devsite-syntax-p">}</span>
<span class="devsite-syntax-w">            </span><span class="devsite-syntax-p">}</span>
<span class="devsite-syntax-w">      </span><span class="devsite-syntax-p">}</span>
<span class="devsite-syntax-w">  </span><span class="devsite-syntax-p">});</span>
<span class="devsite-syntax-p">}</span>
<span class="devsite-syntax-c1">// ..JavaScript code for exporting .wav file for output audio</span>

<span class="devsite-syntax-k">await</span><span class="devsite-syntax-w"> </span><span class="devsite-syntax-nx">main</span><span class="devsite-syntax-p">();</span>
</code></pre></devsite-code></section>
</devsite-selector></div>
<h2 id="voices" data-text="Voice options" tabindex="-1">Voice options</h2>

<p>TTS models support the following 30 voice options in the <code translate="no" dir="ltr">voice_name</code> field:</p>

<div>
<table>
  <colgroup>
    <col class="paid-tier">
    <col>
    <col class="paid-tier">
  </colgroup>
  <tbody>
  <tr>
    <td><b>Zephyr</b> -- <em>Bright</em></td>
    <td><b>Puck</b> -- <em>Upbeat</em></td>
    <td><b>Charon</b> -- <em>Informative</em></td>
  </tr>
  <tr>
    <td><b>Kore</b> -- <em>Firm</em></td>
    <td><b>Fenrir</b> -- <em>Excitable</em></td>
    <td><b>Leda</b> -- <em>Youthful</em></td>
  </tr>
  <tr>
    <td><b>Orus</b> -- <em>Firm</em></td>
    <td><b>Aoede</b> -- <em>Breezy</em></td>
    <td><b>Callirrhoe</b> -- <em>Easy-going</em></td>
  </tr>
  <tr>
    <td><b>Autonoe</b> -- <em>Bright</em></td>
    <td><b>Enceladus</b> -- <em>Breathy</em></td>
    <td><b>Iapetus</b> -- <em>Clear</em></td>
  </tr>
  <tr>
    <td><b>Umbriel</b> -- <em>Easy-going</em></td>
    <td><b>Algieba</b> -- <em>Smooth</em></td>
    <td><b>Despina</b> -- <em>Smooth</em></td>
  </tr>
  <tr>
    <td><b>Erinome</b> -- <em>Clear</em></td>
    <td><b>Algenib</b> -- <em>Gravelly</em></td>
    <td><b>Rasalgethi</b> -- <em>Informative</em></td>
  </tr>
  <tr>
    <td><b>Laomedeia</b> -- <em>Upbeat</em></td>
    <td><b>Achernar</b> -- <em>Soft</em></td>
    <td><b>Alnilam</b> -- <em>Firm</em></td>
  </tr>
  <tr>
    <td><b>Schedar</b> -- <em>Even</em></td>
    <td><b>Gacrux</b> -- <em>Mature</em></td>
    <td><b>Pulcherrima</b> -- <em>Forward</em></td>
  </tr>
  <tr>
    <td><b>Achird</b> -- <em>Friendly</em></td>
    <td><b>Zubenelgenubi</b> -- <em>Casual</em></td>
    <td><b>Vindemiatrix</b> -- <em>Gentle</em></td>
  </tr>
  <tr>
    <td><b>Sadachbia</b> -- <em>Lively</em></td>
    <td><b>Sadaltager</b> -- <em>Knowledgeable</em></td>
    <td><b>Sulafat</b> -- <em>Warm</em></td>
  </tr>
  </tbody>
</table>
</div>

<p>You can hear all the voice options in
<a href="https://aistudio.google.com/generate-speech">AI Studio</a>.</p>

<h2 id="languages" data-text="Supported languages" tabindex="-1">Supported languages</h2>

<p>The TTS models detect the input language automatically. The following languages
are supported:</p>

<table>
    <colgroup>
      <col class="paid-tier">
      <col>
      <col class="paid-tier">
      <col>
   </colgroup>
    <thead>
      <tr>
        <th>Language</th>
        <th>BCP-47 Code</th>
        <th>Language</th>
        <th>BCP-47 Code</th>
      </tr>
    </thead>
    <tbody class="list">
      <tr>
        <td>Arabic</td>
        <td>ar</td>
        <td>Filipino</td>
        <td>fil</td>
      </tr>
      <tr>
        <td>Bangla</td>
        <td>bn</td>
        <td>Finnish</td>
        <td>fi</td>
      </tr>
      <tr>
        <td>Dutch</td>
        <td>nl</td>
        <td>Galician</td>
        <td>gl</td>
      </tr>
      <tr>
        <td>English</td>
        <td>en</td>
        <td>Georgian</td>
        <td>ka</td>
      </tr>
      <tr>
        <td>French</td>
        <td>fr</td>
        <td>Greek</td>
        <td>el</td>
      </tr>
      <tr>
        <td>German</td>
        <td>de</td>
        <td>Gujarati</td>
        <td>gu</td>
      </tr>
      <tr>
        <td>Hindi</td>
        <td>hi</td>
        <td>Haitian Creole</td>
        <td>ht</td>
      </tr>
      <tr>
        <td>Indonesian</td>
        <td>id</td>
        <td>Hebrew</td>
        <td>he</td>
      </tr>
      <tr>
        <td>Italian</td>
        <td>it</td>
        <td>Hungarian</td>
        <td>hu</td>
      </tr>
      <tr>
        <td>Japanese</td>
        <td>ja</td>
        <td>Icelandic</td>
        <td>is</td>
      </tr>
      <tr>
        <td>Korean</td>
        <td>ko</td>
        <td>Javanese</td>
        <td>jv</td>
      </tr>
      <tr>
        <td>Marathi</td>
        <td>mr</td>
        <td>Kannada</td>
        <td>kn</td>
      </tr>
      <tr>
        <td>Polish</td>
        <td>pl</td>
        <td>Konkani</td>
        <td>kok</td>
      </tr>
      <tr>
        <td>Portuguese</td>
        <td>pt</td>
        <td>Lao</td>
        <td>lo</td>
      </tr>
      <tr>
        <td>Romanian</td>
        <td>ro</td>
        <td>Latin</td>
        <td>la</td>
      </tr>
      <tr>
        <td>Russian</td>
        <td>ru</td>
        <td>Latvian</td>
        <td>lv</td>
      </tr>
      <tr>
        <td>Spanish</td>
        <td>es</td>
        <td>Lithuanian</td>
        <td>lt</td>
      </tr>
      <tr>
        <td>Tamil</td>
        <td>ta</td>
        <td>Luxembourgish</td>
        <td>lb</td>
      </tr>
      <tr>
        <td>Telugu</td>
        <td>te</td>
        <td>Macedonian</td>
        <td>mk</td>
      </tr>
      <tr>
        <td>Thai</td>
        <td>th</td>
        <td>Maithili</td>
        <td>mai</td>
      </tr>
      <tr>
        <td>Turkish</td>
        <td>tr</td>
        <td>Malagasy</td>
        <td>mg</td>
      </tr>
      <tr>
        <td>Ukrainian</td>
        <td>uk</td>
        <td>Malay</td>
        <td>ms</td>
      </tr>
      <tr>
        <td>Vietnamese</td>
        <td>vi</td>
        <td>Malayalam</td>
        <td>ml</td>
      </tr>
      <tr>
        <td>Afrikaans</td>
        <td>af</td>
        <td>Mongolian</td>
        <td>mn</td>
      </tr>
      <tr>
        <td>Albanian</td>
        <td>sq</td>
        <td>Nepali</td>
        <td>ne</td>
      </tr>
      <tr>
        <td>Amharic</td>
        <td>am</td>
        <td>Norwegian, Bokmål</td>
        <td>nb</td>
      </tr>
      <tr>
        <td>Armenian</td>
        <td>hy</td>
        <td>Norwegian, Nynorsk</td>
        <td>nn</td>
      </tr>
      <tr>
        <td>Azerbaijani</td>
        <td>az</td>
        <td>Odia</td>
        <td>or</td>
      </tr>
      <tr>
        <td>Basque</td>
        <td>eu</td>
        <td>Pashto</td>
        <td>ps</td>
      </tr>
      <tr>
        <td>Belarusian</td>
        <td>be</td>
        <td>Persian</td>
        <td>fa</td>
      </tr>
      <tr>
        <td>Bulgarian</td>
        <td>bg</td>
        <td>Punjabi</td>
        <td>pa</td>
      </tr>
      <tr>
        <td>Burmese</td>
        <td>my</td>
        <td>Serbian</td>
        <td>sr</td>
      </tr>
      <tr>
        <td>Catalan</td>
        <td>ca</td>
        <td>Sindhi</td>
        <td>sd</td>
      </tr>
      <tr>
        <td>Cebuano</td>
        <td>ceb</td>
        <td>Sinhala</td>
        <td>si</td>
      </tr>
      <tr>
        <td>Chinese, Mandarin</td>
        <td>cmn</td>
        <td>Slovak</td>
        <td>sk</td>
      </tr>
      <tr>
        <td>Croatian</td>
        <td>hr</td>
        <td>Slovenian</td>
        <td>sl</td>
      </tr>
      <tr>
        <td>Czech</td>
        <td>cs</td>
        <td>Swahili</td>
        <td>sw</td>
      </tr>
      <tr>
        <td>Danish</td>
        <td>da</td>
        <td>Swedish</td>
        <td>sv</td>
      </tr>
      <tr>
        <td>Estonian</td>
        <td>et</td>
        <td>Urdu</td>
        <td>ur</td>
      </tr>
    </tbody>
  </table>

<h2 id="supported-models" data-text="Supported models" tabindex="-1">Supported models</h2>

<table>
<thead>
<tr>
<th style="text-align: left">Model</th>
<th style="text-align: left">Single speaker</th>
<th style="text-align: left">Multispeaker</th>
</tr>
</thead>

<tbody>
<tr>
<td style="text-align: left"><a href="/gemini-api/docs/models/gemini-3.1-flash-tts-preview">Gemini 3.1 Flash TTS Preview</a></td>
<td style="text-align: left">✔️</td>
<td style="text-align: left">✔️</td>
</tr>
<tr>
<td style="text-align: left"><a href="/gemini-api/docs/models/gemini-2.5-flash-preview-tts">Gemini 2.5 Flash Preview TTS</a></td>
<td style="text-align: left">✔️</td>
<td style="text-align: left">✔️</td>
</tr>
<tr>
<td style="text-align: left"><a href="/gemini-api/docs/models/gemini-2.5-pro-preview-tts">Gemini 2.5 Pro Preview TTS</a></td>
<td style="text-align: left">✔️</td>
<td style="text-align: left">✔️</td>
</tr>
</tbody>
</table>

<h2 id="prompting-guide" data-text="Prompting guide" tabindex="-1">Prompting guide</h2>

<p>The <strong>Gemini Native Audio Generation Text-to-Speech (TTS)</strong> model differentiates
itself from traditional TTS models by using a large language model that
knows <strong><em>not only what to say, but also how to say it</em></strong>.</p>

<p>Out of the box, the model will natively interpret a transcript and determine how
your words should be delivered. Simple transcripts without any additional
prompting sound natural. But Gemini TTS also comes with tools you can use to
steer it.</p>

<p>The purpose of this guide is to offer fundamental direction and spark ideas when
developing audio experiences. We&#39;ll start with <strong>Tags</strong> for quick inline
control, and then explore advanced <strong>Prompting structures</strong> for full performance
direction.</p>

<h3 id="audio-tags" data-text="Audio tags" tabindex="-1">Audio tags</h3>

<p>Tags are inline modifiers like <code translate="no" dir="ltr">[whispers]</code> or <code translate="no" dir="ltr">[laughs]</code> that give you granular
control over the delivery. You can use them to change the tone, pace, and
emotional vibe of a line or section of the transcript. You can also use them to
add interjections and a few other non-verbal sounds to the performance, like
<code translate="no" dir="ltr">[cough]</code>, <code translate="no" dir="ltr">[sighs]</code> or <code translate="no" dir="ltr">[gasp]</code>.</p>

<p>There is no exhaustive list on what tags do and don&#39;t work, we recommend
experimenting with different emotions and expressions to see how the output
changes.</p>

<p>If your transcript is not in English, for best results we recommend that you
still use English audio tags.</p>

<p><strong>Be creative with audio tags</strong></p>

<p>To show the kind of variability you can get with audio tags, here are a set of
examples that each say the same thing, but the delivery changes based on the
tags used.</p>

<p>You can change the emphasis of the delivery by adding tags at the start of a
line to make the speaker excited, bored, or reluctant:</p>

<ul>
<li><code translate="no" dir="ltr">[excitedly]</code> Hey there, I&#39;m a new text to speech model, and I can say things
in many different ways. How can I help you today?</li>
<li><code translate="no" dir="ltr">[bored]</code> Hey there, I&#39;m a new text to speech model…</li>
<li><code translate="no" dir="ltr">[reluctantly]</code> Hey there, I&#39;m a new text to speech model…</li>
</ul>

<p>Tags can also be used to change the pace of the delivery, or to combine pace
with emphasis:</p>

<ul>
<li><code translate="no" dir="ltr">[very fast]</code> Hey there, I&#39;m a new text to speech model…</li>
<li><code translate="no" dir="ltr">[very slow]</code> Hey there, I&#39;m a new text to speech model…</li>
<li><code translate="no" dir="ltr">[sarcastically, one painfully slow word at a time]</code> Hey there, I&#39;m a new text
to speech model…</li>
</ul>

<p>You also have precise control over specific sections, meaning you can whisper
one part and shout another.</p>

<ul>
<li><code translate="no" dir="ltr">[whispers]</code> Hey there, I&#39;m a new text to speech model, <code translate="no" dir="ltr">[shouting]</code> and I can
say things in many different ways. <code translate="no" dir="ltr">[whispers]</code> How can I help you today</li>
</ul>

<p>You can also experiment with any creative idea you want:</p>

<ul>
<li><code translate="no" dir="ltr">[like a cartoon dog]</code> Hey there, I&#39;m a new text to speech model…</li>
<li><code translate="no" dir="ltr">[like dracula]</code> Hey there, I&#39;m a new text to speech model…</li>
</ul>

<p>Commonly used tags include:</p>

<div>
<table>
  <colgroup>
    <col class="paid-tier">
    <col>
    <col class="paid-tier">
    <col>
  </colgroup>
  <tbody>
  <tr>
    <td><code translate="no" dir="ltr">[amazed]</code></td>
    <td><code translate="no" dir="ltr">[crying]</code></td>
    <td><code translate="no" dir="ltr">[curious]</code></td>
    <td><code translate="no" dir="ltr">[excited]</code></td>
  </tr>
  <tr>
    <td><code translate="no" dir="ltr">[sighs]</code></td>
    <td><code translate="no" dir="ltr">[gasp]</code></td>
    <td><code translate="no" dir="ltr">[giggles]</code></td>
    <td><code translate="no" dir="ltr">[laughs]</code></td>
  </tr>
  <tr>
    <td><code translate="no" dir="ltr">[mischievously]</code></td>
    <td><code translate="no" dir="ltr">[panicked]</code></td>
    <td><code translate="no" dir="ltr">[sarcastic]</code></td>
    <td><code translate="no" dir="ltr">[serious]</code></td>
  </tr>
  <tr>
    <td><code translate="no" dir="ltr">[shouting]</code></td>
    <td><code translate="no" dir="ltr">[tired]</code></td>
    <td><code translate="no" dir="ltr">[trembling]</code></td>
    <td><code translate="no" dir="ltr">[whispers]</code></td>
  </tr>
  </tbody>
</table>
</div>

<p>Tags give quick and easy control over the delivery of your transcript. For even
more control, you can combine them with a context prompt to set the overall tone
 and vibe of the performance.</p>

<h3 id="advanced-prompting" data-text="Advanced prompting" tabindex="-1">Advanced prompting</h3>

<p>You can think of an advanced prompt as a system instruction for the model to
follow. It&#39;s a way to give the model more context and control over the
performance.</p>

<p>A robust prompt ideally includes the following elements that come together to
craft a great performance:</p>

<ul>
<li><strong>Audio Profile</strong> - Establishes a persona for the voice, defining a character
identity, archetype and any other characteristics like age, background etc.</li>
<li><strong>Scene</strong> - Sets the stage. Describes both the physical environment and the
&quot;vibe&quot;.</li>
<li><strong>Director&#39;s Notes</strong> - Performance guidance where you can break down which
instructions are important for your virtual talent to take note of. Examples are
style, breathing, pacing, articulation and accent.</li>
<li><strong>Sample context</strong> - Gives the model a contextual starting point, so your
virtual actor enters the scene you set up naturally.</li>
<li><strong>Transcript</strong> - The text that the model will speak out. For best performance,
remember that the transcript topic and writing style should correlate to the
directions you are giving.</li>
<li><strong>Audio tags</strong> - Modifiers you can put into a transcript to change how that
part of the text is delivered, such as <code translate="no" dir="ltr">[whispers]</code> or <code translate="no" dir="ltr">[shouting]</code>.</li>
</ul>
<aside class="note"><strong>Note:</strong><span> Have Gemini help you build your prompt, just give it a blank outline of
the format below and ask it to sketch out a character for you.</span></aside>
<p>Example full prompt:</p>
<div></div><devsite-code><pre class="devsite-click-to-copy" translate="no" dir="ltr" is-upgraded syntax="Markdown"><code translate="no" dir="ltr"><span class="devsite-syntax-gh"># AUDIO PROFILE: Jaz R.</span>
<span class="devsite-syntax-gu">## "The Morning Hype"</span>

<span class="devsite-syntax-gu">## THE SCENE: The London Studio</span>
It is 10:00 PM in a glass-walled studio overlooking the moonlit London skyline,
but inside, it is blindingly bright. The red "ON AIR" tally light is blazing.
Jaz is standing up, not sitting, bouncing on the balls of their heels to the
rhythm of a thumping backing track. Their hands fly across the faders on a
massive mixing desk. It is a chaotic, caffeine-fueled cockpit designed to wake
up an entire nation.

<span class="devsite-syntax-gu">### DIRECTOR'S NOTES</span>
Style:
<span class="devsite-syntax-k">*</span><span class="devsite-syntax-w"> </span>The "Vocal Smile": You must hear the grin in the audio. The soft palate is
always raised to keep the tone bright, sunny, and explicitly inviting.
<span class="devsite-syntax-k">*</span><span class="devsite-syntax-w"> </span>Dynamics: High projection without shouting. Punchy consonants and elongated
vowels on excitement words (e.g., "Beauuutiful morning").

Pace: Speaks at an energetic pace, keeping up with the fast music.  Speaks
with A "bouncing" cadence. High-speed delivery with fluid transitions — no dead
air, no gaps.

Accent: Jaz is from Brixton, London

<span class="devsite-syntax-gu">### SAMPLE CONTEXT</span>
Jaz is the industry standard for Top 40 radio, high-octane event promos, or any
script that requires a charismatic Estuary accent and 11/10 infectious energy.

<span class="devsite-syntax-gu">#### TRANSCRIPT</span>
[excitedly] Yes, massive vibes in the studio! You are locked in and it is
absolutely popping off in London right now. If you're stuck on the tube, or
just sat there pretending to work... stop it. Seriously, I see you.
[shouting] Turn this up! We've got the project roadmap landing in three,
two... let's go!
</code></pre></devsite-code>
<h3 id="prompting-strategies" data-text="Detailed prompting strategies" tabindex="-1">Detailed prompting strategies</h3>

<p>Let&#39;s break down each element of the prompt.</p>

<h4 id="audio-profile" data-text="Audio Profile" tabindex="-1">Audio Profile</h4>

<p>Briefly describe the persona of the character.</p>

<ul>
<li><strong>Name.</strong> Giving your character a name helps ground the model and tight
performance together, Refer to the character by name when setting the scene and
context</li>
<li><strong>Role.</strong> Core identity and archetype of the character that&#39;s playing out
in the scene. e.g., Radio DJ, Podcaster, News reporter etc.</li>
</ul>

<p>Examples:</p>
<div></div><devsite-code><pre class="devsite-click-to-copy" translate="no" dir="ltr" is-upgraded syntax="Markdown"><code translate="no" dir="ltr"><span class="devsite-syntax-gh"># AUDIO PROFILE: Jaz R.</span>
<span class="devsite-syntax-gu">## "The Morning Hype"</span>
</code></pre></devsite-code>
<p><br></p>
<div></div><devsite-code><pre class="devsite-click-to-copy" translate="no" dir="ltr" is-upgraded syntax="Markdown"><code translate="no" dir="ltr"><span class="devsite-syntax-gh"># AUDIO PROFILE: Monica A.</span>
<span class="devsite-syntax-gu">## "The Beauty Influencer"</span>
</code></pre></devsite-code>
<h4 id="scene" data-text="Scene" tabindex="-1">Scene</h4>

<p>Set the context for the scene, including location, mood, and environmental
details that establish the tone and vibe. Describe what is happening around the
character and how it affects them. The scene provides the environmental context
for the entire interaction and guides the acting performance in a subtle
organic way.</p>

<p>Examples:</p>
<div></div><devsite-code><pre class="devsite-click-to-copy" translate="no" dir="ltr" is-upgraded syntax="Markdown"><code translate="no" dir="ltr"><span class="devsite-syntax-gu">## THE SCENE: The London Studio</span>
It is 10:00 PM in a glass-walled studio overlooking the moonlit London skyline,
but inside, it is blindingly bright. The red "ON AIR" tally light is blazing.
Jaz is standing up, not sitting, bouncing on the balls of their heels to the
rhythm of a thumping backing track. Their hands fly across the faders on a
massive mixing desk. It is a chaotic, caffeine-fueled cockpit designed to
wake up an entire nation.
</code></pre></devsite-code>
<p><br></p>
<div></div><devsite-code><pre class="devsite-click-to-copy" translate="no" dir="ltr" is-upgraded syntax="Markdown"><code translate="no" dir="ltr"><span class="devsite-syntax-gu">## THE SCENE: Homegrown Studio</span>
A meticulously sound-treated bedroom in a suburban home. The space is
deadened by plush velvet curtains and a heavy rug, but there is a
distinct "proximity effect."
</code></pre></devsite-code>
<h4 id="directors-notes" data-text="Directors notes" tabindex="-1">Directors notes</h4>

<p>This critical section includes specific performance guidance. You can skip all
the other elements, but we recommend you include this element.</p>

<p>Define only what&#39;s important to the performance, being careful to not
overspecify. Too many strict rules will limit the models&#39; creativity and may
result in a worse performance. Balance the role and scene description with the
specific performance rules.</p>

<p>The most common directions are <strong>Style, Pacing and Accent</strong>, but the model is
not limited to these, nor requires them. Feel free to include custom
instructions to cover any additional details important to your performance, and
go into as much or as little detail as necessary.</p>

<p>For example:</p>
<div></div><devsite-code><pre class="devsite-click-to-copy" translate="no" dir="ltr" is-upgraded syntax="Markdown"><code translate="no" dir="ltr"><span class="devsite-syntax-gu">### DIRECTOR'S NOTES</span>

Style: Enthusiastic and Sassy GenZ beauty YouTuber

Pacing: Speaks at an energetic pace, keeping up with the extremely fast, rapid
delivery influencers use in short form videos.

Accent: Southern california valley girl from Laguna Beach |
</code></pre></devsite-code>
<p><strong>Style:</strong></p>

<p>Sets the tone and Style of the generated speech. Include things like upbeat,
energetic, relaxed, bored etc. to guide the performance. Be descriptive and
provide as much detail as necessary:  <em>&quot;Infectious enthusiasm. The listener
should feel like they are part of a massive, exciting community event.&quot;</em> works
better than simply saying <em>&quot;energetic and enthusiastic&quot;.</em></p>

<p>You can even try terms that are popular in the voiceover industry, like &quot;vocal
smile&quot;. You can layer as many style characteristics as you want.</p>

<p>Examples:</p>

<p>Simple Emotion</p>
<div></div><devsite-code><pre class="devsite-click-to-copy" translate="no" dir="ltr" is-upgraded syntax="Markdown"><code translate="no" dir="ltr">DIRECTORS NOTES
...
Style: Frustrated and angry developer who can't get the build to run.
...
</code></pre></devsite-code>
<p>More depth</p>
<div></div><devsite-code><pre class="devsite-click-to-copy" translate="no" dir="ltr" is-upgraded syntax="Markdown"><code translate="no" dir="ltr">DIRECTORS NOTES
...
Style: Sassy GenZ beauty YouTuber, who mostly creates content for YouTube Shorts.
...
</code></pre></devsite-code>
<p>Complex</p>
<div></div><devsite-code><pre class="devsite-click-to-copy" translate="no" dir="ltr" is-upgraded syntax="Markdown"><code translate="no" dir="ltr">DIRECTORS NOTES
Style:
<span class="devsite-syntax-k">*</span><span class="devsite-syntax-w"> </span>The "Vocal Smile": You must hear the grin in the audio. The soft palate is
always raised to keep the tone bright, sunny, and explicitly inviting.
*Dynamics: High projection without shouting. Punchy consonants and
elongated vowels on excitement words (e.g., "Beauuutiful morning").
</code></pre></devsite-code>
<p><strong>Accent:</strong></p>

<p>Describe the desired accent. The more specific you are, the better the
results are. For example use &quot;<em>British English accent as heard in Croydon,
England</em>&quot; vs &quot;<em>British Accent</em>&quot;.</p>

<p>Examples:</p>
<div></div><devsite-code><pre class="devsite-click-to-copy" translate="no" dir="ltr" is-upgraded syntax="Markdown"><code translate="no" dir="ltr"><span class="devsite-syntax-gu">### DIRECTORS NOTES</span>
...
Accent: Southern california valley girl from Laguna Beach
...
</code></pre></devsite-code>
<p><br></p>
<div></div><devsite-code><pre class="devsite-click-to-copy" translate="no" dir="ltr" is-upgraded syntax="Markdown"><code translate="no" dir="ltr"><span class="devsite-syntax-gu">### DIRECTORS NOTES</span>
...
Accent: Jaz is a DJ from Brixton, London
...
</code></pre></devsite-code>
<p><strong>Pacing:</strong></p>

<p>Overall pacing and pace variation throughout the piece.</p>

<p>Examples:</p>

<p>Simple</p>
<div></div><devsite-code><pre class="devsite-click-to-copy" translate="no" dir="ltr" is-upgraded syntax="Markdown"><code translate="no" dir="ltr"><span class="devsite-syntax-gu">### DIRECTORS NOTES</span>
...
Pacing: Speak as fast as possible
...
</code></pre></devsite-code>
<p>More Depth</p>
<div></div><devsite-code><pre class="devsite-click-to-copy" translate="no" dir="ltr" is-upgraded syntax="Markdown"><code translate="no" dir="ltr"><span class="devsite-syntax-gu">### DIRECTORS NOTES</span>
...
Pacing: Speaks at a faster, energetic pace, keeping up with fast paced music.
...
</code></pre></devsite-code>
<p>Complex</p>
<div></div><devsite-code><pre class="devsite-click-to-copy" translate="no" dir="ltr" is-upgraded syntax="Markdown"><code translate="no" dir="ltr"><span class="devsite-syntax-gu">### DIRECTORS NOTES</span>
...
Pacing: The "Drift": The tempo is incredibly slow and liquid. Words bleed into each other. There is zero urgency.
...
</code></pre></devsite-code>
<h4 id="transcript-tags" data-text="Transcript and audio tags" tabindex="-1">Transcript and audio tags</h4>

<p>The transcript is the exact words the model will speak. An audio tag is a word
in square brackets that indicates either how something should be said, a change
of tone, or an interjection.</p>
<div></div><devsite-code><pre class="devsite-click-to-copy" translate="no" dir="ltr" is-upgraded syntax="Markdown"><code translate="no" dir="ltr"><span class="devsite-syntax-gu">### TRANSCRIPT</span>

I know right, [sarcastically] I couldn't believe it. [whispers] She should have totally left
at that point.

[cough] Well, [sighs] I guess it doesn't matter now.
</code></pre></devsite-code>
<p><strong>Give it a try</strong></p>

<p>Try some of these examples yourself on
<a href="https://aistudio.google.com/generate-speech">AI Studio</a>, play with our
<a href="http://aistudio.google.com/app/apps/bundled/synergy_intro">TTS App</a> and let
Gemini put you in the directors chair. Keep these tips in mind to make great
vocal performances:</p>

<ul>
<li>Remember to keep the entire prompt coherent – the script and direction go hand in hand in creating a great performance.</li>
<li>Don&#39;t feel you have to describe everything, sometimes giving the model space to fill in the gaps helps naturalness. (Just like a talented actor)</li>
<li>If you ever are feeling stuck, have Gemini lend you a hand to help you craft your script or performance.</li>
</ul>

<h2 id="limitations" data-text="Limitations" tabindex="-1">Limitations</h2>

<ul>
<li>TTS models can only receive text inputs and generate audio outputs.</li>
<li>A TTS session has a <a href="/gemini-api/docs/long-context">context window</a> limit of
32k tokens.</li>
<li>Review <a href="/gemini-api/docs/speech-generation#languages">Languages</a> section for language support.</li>
<li>TTS does not support streaming.</li>
</ul>

<p>The following constraints apply specifically when using the Gemini 3.1 Flash
TTS Preview model for speech generation:</p>

<ul>
<li><strong>Voice inconsistency with prompt instructions:</strong> The model&#39;s output may not
always strictly match the selected speaker, causing the audio to sound
different than expected. To avoid mismatched tones (such as a deep male
voice attempting to speak like a young girl), ensure your prompt&#39;s written
tone and context align naturally with the selected speaker&#39;s profile.</li>
<li><strong>Quality of longer outputs:</strong> Speech quality and consistency may begin to
drift with generated outputs that are longer than a few minutes. We
recommend splitting your transcripts into smaller chunks.</li>
<li><strong>Occasional text token returns:</strong> The model occasionally returns text tokens
instead of audio tokens, causing the server to fail the request with a <code translate="no" dir="ltr">500</code>
error. Because this occurs randomly in a very small percentage of requests,
you should implement automated retry logic in your application to handle
these.</li>
<li><strong>Prompt classifier false rejections:</strong> Vague prompts may fail to trigger
the speech synthesis classifier, resulting in a rejected request
(<code translate="no" dir="ltr">PROHIBITED_CONTENT</code>) or causing the model to read your style instructions
and director&#39;s notes aloud. Validate your prompts by adding a clear preamble
instructing the model to synthesize speech, and explicitly label where the
actual spoken transcript begins.</li>
</ul>

<h2 id="whats-next" data-text="What's next" tabindex="-1">What's next</h2>

<ul>
<li>Try the <a href="https://colab.research.google.com/github/google-gemini/cookbook/blob/main/quickstarts/Get_started_TTS.ipynb">audio generation cookbook</a>.</li>
<li>Gemini&#39;s <a href="/gemini-api/docs/live">Live API</a> offers interactive audio
generation options you can interleave with other modalities.</li>
<li>For working with audio <em>inputs</em>, visit the <a href="/gemini-api/docs/audio">Audio understanding</a> guide.</li>
</ul>
<link href="https://fonts.googleapis.com/css2?family=Google+Symbols:opsz,wght,FILL,GRAD@20..48,100..700,0..1,-50..200" rel="stylesheet" data-page-link>
  

  
</div>

  
    
    
      
    <devsite-thumb-rating position="footer">
    </devsite-thumb-rating>
  
       
         <devsite-feedback
  position="footer"
  project-name="Gemini API"
  product-id="5292923"
  bucket="documentation"
  context=""
  version="t-devsite-webserver-20260528-r00-rc00.477908439157110416"
  data-label="Send Feedback Button"
  track-type="feedback"
  track-name="sendFeedbackLink"
  track-metadata-position="footer"
  class="nocontent"
  data-nosnippet
  
  
  
    project-icon="https://www.gstatic.com/devrel-devsite/prod/v5b93ab110c02dc91cc5b79fb160a3c37758bb2dfb04b22b9173ffe5646621934/googledevai/images/touchicon-180-new.png"
  
  
  
  >

  <button>
  
    
    Send feedback
  
  </button>
</devsite-feedback>
       
    
    
  

  <div class="devsite-floating-action-buttons"></div></article>


<devsite-content-footer class="nocontent" data-nosnippet>
  <p>Except as otherwise noted, the content of this page is licensed under the <a href="https://creativecommons.org/licenses/by/4.0/">Creative Commons Attribution 4.0 License</a>, and code samples are licensed under the <a href="https://www.apache.org/licenses/LICENSE-2.0">Apache 2.0 License</a>. For details, see the <a href="https://developers.google.com/site-policies">Google Developers Site Policies</a>. Java is a registered trademark of Oracle and/or its affiliates.</p>
  <p>Last updated 2026-05-18 UTC.</p>
</devsite-content-footer>


<devsite-notification
>
</devsite-notification>


  
<div class="devsite-content-data">
  
    
    
    <template class="devsite-thumb-rating-feedback">
      <devsite-feedback
  position="thumb-rating"
  project-name="Gemini API"
  product-id="5292923"
  bucket="documentation"
  context=""
  version="t-devsite-webserver-20260528-r00-rc00.477908439157110416"
  data-label="Send Feedback Button"
  track-type="feedback"
  track-name="sendFeedbackLink"
  track-metadata-position="thumb-rating"
  class="nocontent"
  data-nosnippet
  
  
  
    project-icon="https://www.gstatic.com/devrel-devsite/prod/v5b93ab110c02dc91cc5b79fb160a3c37758bb2dfb04b22b9173ffe5646621934/googledevai/images/touchicon-180-new.png"
  
  
  
  >

  <button>
  
    Need to tell us more?
  
  </button>
</devsite-feedback>
    </template>
  
  
    <template class="devsite-content-data-template">
      [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Missing the information I need","missingTheInformationINeed","thumb-down"],["Too complicated / too many steps","tooComplicatedTooManySteps","thumb-down"],["Out of date","outOfDate","thumb-down"],["Samples / code issue","samplesCodeIssue","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-05-18 UTC."],[],[]]
    </template>
  
</div>
            
          </devsite-content>
        </main>
        <devsite-footer-promos class="devsite-footer">
          
            
          
        </devsite-footer-promos>
        <devsite-footer-linkboxes class="devsite-footer">
          
            
<nav class="devsite-footer-linkboxes nocontent"
     aria-label="Footer links"
     data-nosnippet>
  
</nav>
          
        </devsite-footer-linkboxes>
        <devsite-footer-utility class="devsite-footer">
          
            

<div class="devsite-footer-utility nocontent" data-nosnippet>
  

  
  <nav class="devsite-footer-utility-links" aria-label="Utility links">
    
    <ul class="devsite-footer-utility-list">
      
      <li class="devsite-footer-utility-item
                 ">
        
        
        <a class="devsite-footer-utility-link gc-analytics-event"
           href="//policies.google.com/terms"
           data-category="Site-Wide Custom Events"
           data-label="Footer Terms link"
         >
          Terms
        </a>
        
      </li>
      
      <li class="devsite-footer-utility-item
                 ">
        
        
        <a class="devsite-footer-utility-link gc-analytics-event"
           href="//policies.google.com/privacy"
           data-category="Site-Wide Custom Events"
           data-label="Footer Privacy link"
         >
          Privacy
        </a>
        
      </li>
      
      <li class="devsite-footer-utility-item
                 glue-cookie-notification-bar-control">
        
        
        <a class="devsite-footer-utility-link gc-analytics-event"
           href="#"
           data-category="Site-Wide Custom Events"
           data-label="Footer Manage cookies link"
         
           aria-hidden="true"
         >
          Manage cookies
        </a>
        
      </li>
      
    </ul>
    
    
<devsite-language-selector>
  <ul role="presentation">
    
    
    <li role="presentation">
      <a role="menuitem" lang="en"
        >English</a>
    </li>
    
    <li role="presentation">
      <a role="menuitem" lang="de"
        >Deutsch</a>
    </li>
    
    <li role="presentation">
      <a role="menuitem" lang="es_419"
        >Español – América Latina</a>
    </li>
    
    <li role="presentation">
      <a role="menuitem" lang="fr"
        >Français</a>
    </li>
    
    <li role="presentation">
      <a role="menuitem" lang="id"
        >Indonesia</a>
    </li>
    
    <li role="presentation">
      <a role="menuitem" lang="it"
        >Italiano</a>
    </li>
    
    <li role="presentation">
      <a role="menuitem" lang="pl"
        >Polski</a>
    </li>
    
    <li role="presentation">
      <a role="menuitem" lang="pt_br"
        >Português – Brasil</a>
    </li>
    
    <li role="presentation">
      <a role="menuitem" lang="sq"
        >Shqip</a>
    </li>
    
    <li role="presentation">
      <a role="menuitem" lang="vi"
        >Tiếng Việt</a>
    </li>
    
    <li role="presentation">
      <a role="menuitem" lang="tr"
        >Türkçe</a>
    </li>
    
    <li role="presentation">
      <a role="menuitem" lang="ru"
        >Русский</a>
    </li>
    
    <li role="presentation">
      <a role="menuitem" lang="he"
        >עברית</a>
    </li>
    
    <li role="presentation">
      <a role="menuitem" lang="ar"
        >العربيّة</a>
    </li>
    
    <li role="presentation">
      <a role="menuitem" lang="fa"
        >فارسی</a>
    </li>
    
    <li role="presentation">
      <a role="menuitem" lang="hi"
        >हिंदी</a>
    </li>
    
    <li role="presentation">
      <a role="menuitem" lang="bn"
        >বাংলা</a>
    </li>
    
    <li role="presentation">
      <a role="menuitem" lang="th"
        >ภาษาไทย</a>
    </li>
    
    <li role="presentation">
      <a role="menuitem" lang="zh_cn"
        >中文 – 简体</a>
    </li>
    
    <li role="presentation">
      <a role="menuitem" lang="zh_tw"
        >中文 – 繁體</a>
    </li>
    
    <li role="presentation">
      <a role="menuitem" lang="ja"
        >日本語</a>
    </li>
    
    <li role="presentation">
      <a role="menuitem" lang="ko"
        >한국어</a>
    </li>
    
  </ul>
</devsite-language-selector>

  </nav>
</div>
          
        </devsite-footer-utility>
        <devsite-panel>
          
        </devsite-panel>
        
      </section>
      </section>
    <devsite-sitemask></devsite-sitemask>
    <devsite-snackbar></devsite-snackbar>
    <devsite-tooltip ></devsite-tooltip>
    <devsite-heading-link></devsite-heading-link>
    <devsite-analytics>
      
        <script type="application/json" analytics>[]</script>
<script type="application/json" tag-management>{&#34;at&#34;: &#34;True&#34;, &#34;ga4&#34;: [], &#34;ga4p&#34;: [], &#34;gtm&#34;: [{&#34;id&#34;: &#34;GTM-TC2MQKS8&#34;, &#34;purpose&#34;: 0}], &#34;parameters&#34;: {&#34;internalUser&#34;: &#34;False&#34;, &#34;language&#34;: {&#34;machineTranslated&#34;: &#34;False&#34;, &#34;requested&#34;: &#34;en&#34;, &#34;served&#34;: &#34;en&#34;}, &#34;pageType&#34;: &#34;article&#34;, &#34;projectName&#34;: &#34;Gemini API&#34;, &#34;signedIn&#34;: &#34;False&#34;, &#34;tenant&#34;: &#34;googledevai&#34;, &#34;recommendations&#34;: {&#34;sourcePage&#34;: &#34;&#34;, &#34;sourceType&#34;: 0, &#34;sourceRank&#34;: 0, &#34;sourceIdenticalDescriptions&#34;: 0, &#34;sourceTitleWords&#34;: 0, &#34;sourceDescriptionWords&#34;: 0, &#34;experiment&#34;: &#34;&#34;}, &#34;experiment&#34;: {&#34;ids&#34;: &#34;&#34;}}}</script>
      
    </devsite-analytics>
    
      <devsite-badger></devsite-badger>
    
    
    
    
<script nonce="mG6U0QkZPHK+WMLo7My7sfPuizIRkI">
  
  (function(d,e,v,s,i,t,E){d['GoogleDevelopersObject']=i;
    t=e.createElement(v);t.async=1;t.src=s;E=e.getElementsByTagName(v)[0];
    E.parentNode.insertBefore(t,E);})(window, document, 'script',
    'https://www.gstatic.com/devrel-devsite/prod/v5b93ab110c02dc91cc5b79fb160a3c37758bb2dfb04b22b9173ffe5646621934/googledevai/js/app_loader.js', '[59,"en",null,"/js/devsite_app_module.js","https://www.gstatic.com/devrel-devsite/prod/v5b93ab110c02dc91cc5b79fb160a3c37758bb2dfb04b22b9173ffe5646621934","https://www.gstatic.com/devrel-devsite/prod/v5b93ab110c02dc91cc5b79fb160a3c37758bb2dfb04b22b9173ffe5646621934/googledevai","https://googledevai-dot-devsite-v2-prod-3p.appspot.com",null,null,["/_pwa/googledevai/manifest.json","https://www.gstatic.com/devrel-devsite/prod/v5b93ab110c02dc91cc5b79fb160a3c37758bb2dfb04b22b9173ffe5646621934/images/video-placeholder.svg","https://www.gstatic.com/devrel-devsite/prod/v5b93ab110c02dc91cc5b79fb160a3c37758bb2dfb04b22b9173ffe5646621934/googledevai/images/favicon-new.png","/_static/googledevai/images/gemini-api-logo.svg","https://fonts.googleapis.com/css?family=Google+Sans:400,500|Roboto:400,400italic,500,500italic,700,700italic|Roboto+Mono:400,500,700|Inter:400,500|Inter+Tight:300,500,600&display=swap"],1,null,[1,6,8,12,14,17,21,25,50,52,63,70,75,76,80,87,91,92,93,97,98,100,101,102,103,104,105,107,108,109,110,112,113,117,118,120,122,124,125,126,127,129,130,131,132,133,134,135,136,138,140,141,147,148,149,151,152,156,157,158,159,161,163,164,168,169,170,179,180,182,183,186,191,193,196],"AIzaSyCNm9YxQumEXwGJgTDjxoxXK6m1F-9720Q","AIzaSyCc76DZePGtoyUjqKrLdsMGk_ry7sljLbY","ai.google.dev","AIzaSyB9bqgQ2t11WJsOX8qNsCQ6U-w91mmqF-I","AIzaSyAdYnStPdzjcJJtQ0mvIaeaMKj7_t6J_Fg",null,null,null,["DevPro__enable_google_payments_buyflow","CloudShell__cloud_shell_button","Analytics__enable_clearcut_logging","Profiles__enable_page_saving","MiscFeatureFlags__enable_view_transitions","DevPro__enable_nvidia_credits_card","DevPro__remove_eu_tax_intake_form","SignIn__enable_l1_signup_flow","Profiles__enable_join_program_group_endpoint","Profiles__enable_complete_playlist_endpoint","Profiles__enable_completequiz_endpoint","DevPro__enable_devsite_captcha","Cloud__enable_cloud_shell","EngEduTelemetry__enable_engedu_telemetry","DevPro__enable_enterprise","Profiles__enable_public_developer_profiles","Profiles__enable_purchase_prompts","Search__enable_page_map","DevPro__enable_devpro_offers","MiscFeatureFlags__enable_variable_operator","Search__enable_ai_eligibility_checks","Profiles__enable_developer_profile_benefits_ui_redesign","Profiles__enable_playlist_community_acl","Profiles__enable_recognition_badges","Profiles__enable_developer_profiles_callout","Profiles__enable_developer_profile_pages_as_content","Profiles__enable_dashboard_curated_recommendations","DevPro__enable_firebase_workspaces_card","Cloud__enable_cloud_dlp_service","MiscFeatureFlags__developers_footer_dark_image","DevPro__enable_cloud_innovators_plus","DevPro__enable_credits_banner","TpcFeatures__enable_unmirrored_page_left_nav","DevPro__enable_g1_integration","Profiles__enable_profile_collections","Cloud__fast_free_trial","Cloud__enable_cloud_shell_fte_user_flow","MiscFeatureFlags__enable_variable_operator_index_yaml","MiscFeatureFlags__enable_appearance_cookies","Profiles__require_profile_eligibility_for_signin","BookNav__enable_tenant_cache_key","TpcFeatures__proxy_prod_host","DevPro__enable_free_benefits","Concierge__enable_remove_info_panel_tags","Search__enable_suggestions_from_borg","DevPro__enable_code_assist","Concierge__enable_pushui","Profiles__enable_callout_notifications","Concierge__enable_actions_menu","Profiles__enable_user_type","Profiles__enable_stripe_subscription_management","MiscFeatureFlags__enable_framebox_badge_methods","Search__enable_ai_search_summaries_for_all","Profiles__enable_release_notes_notifications","Profiles__enable_completecodelab_endpoint","Experiments__reqs_query_experiments","MiscFeatureFlags__enable_firebase_utm","CloudShell__cloud_code_overflow_menu","Cloud__cache_serialized_dynamic_content","MiscFeatureFlags__enable_project_variables","Search__enable_dynamic_content_confidential_banner","MiscFeatureFlags__enable_llms_txt","MiscFeatureFlags__enable_explicit_template_dependencies","Cloud__enable_llm_concierge_chat","OnSwitch__enable","Cloud__enable_legacy_calculator_redirect","Cloud__enable_cloudx_experiment_ids","Profiles__enable_awarding_url","Analytics__enable_devpro_interaction_logging","Cloud__enable_free_trial_server_call","DevPro__enable_vertex_credit_card","DevPro__enable_developer_subscriptions","Profiles__enable_targeted_hero","MiscFeatureFlags__gdp_dashboard_reskin_enabled","Profiles__enable_auto_apply_credits","DevPro__enable_google_one_card","MiscFeatureFlags__developers_footer_image","MiscFeatureFlags__remove_cross_domain_tracking_params","Concierge__enable_devsite_llm_tools","MiscFeatureFlags__fix_lower_breadcrumbs","DevPro__enable_embed_profile_creation"],null,null,"AIzaSyA58TaKli1DculwmAmbpzLVGuWc8eCQgQc","https://developerscontentserving-pa.googleapis.com","AIzaSyDWBU60w0P9hEkr29kkksYs8Z7gvZ8u_wc","https://developerscontentsearch-pa.googleapis.com",2,4,null,"https://developerprofiles-pa.googleapis.com",[59,"googledevai","Google AI for Developers","ai.google.dev",null,"googledevai-dot-devsite-v2-prod-3p.appspot.com",null,null,[null,1,null,null,null,null,null,null,null,null,null,[1],null,null,null,null,null,null,[1],null,null,null,null,[1],[1,1,null,1,1],null,null,null,null,null,[1]],null,[73,null,null,null,null,null,"/images/lockup-new.svg","/images/touchicon-180-new.png",null,null,null,null,1,1,null,null,null,null,null,null,null,2,null,null,null,"/images/lockup-dark-theme-new.svg",[]],[],null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,[44,2,4,6,7,12,14,15,17,18,20,21,22,23,28,29,32,37,39,40,43],null,[[],[1,1],null,1],[[null,null,null,null,null,["GTM-TC2MQKS8"],null,null,null,null,null,[["GTM-TC2MQKS8",1]],1]],null,4,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,[]],1,null,1,null,"https://developerscontentinsights-pa.googleapis.com","AIzaSyC11xEGtFhkmSh_iF6l_itbxnFz2GrIBOg","AIzaSyAXJ10nRF73mmdSDINgkCNX5bbd2KPcWm8","https://developers.googleapis.com",["https://aistudio.google.com"],null,"AIzaSyCjP0KOnHfv8mwe38sfzZJMOnqE3HvrD4A",null,null,"https://developers.googleapis.com"]')
  
</script>

    <devsite-a11y-announce></devsite-a11y-announce>
  </body>
</html>


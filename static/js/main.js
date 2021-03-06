/*-----------------------------------------------------------------------------------

  Template Name: Tmart-Minimalist eCommerce HTML5 Template.
  Template URI: #
  Description: Tmart is a unique website template designed in HTML with a simple & beautiful look. There is an excellent solution for creating clean, wonderful and trending material design corporate, corporate any other purposes websites.
  Author: Theme365
  Version: 1.0

-----------------------------------------------------------------------------------*/

/*-------------------------------
[  Table of contents  ]
---------------------------------
  01. jQuery MeanMenu
  02. wow js active
  03. Portfolio  Masonry (width)
  04. Sticky Header
  05. ScrollUp
  06. Tooltip
  07. ScrollReveal Js Init
  08. Fixed Footer bottom script ( Newsletter )
  09. Search Bar
  10. Toogle Menu
  11. Shopping Cart Area
  12. Filter Area
  13. User Menu
  14. Overlay Close
  15. Home Slider 
  16. Popular Product Wrap
  17. Testimonial Wrap
  18. Magnific Popup  
  19. Price Slider Active
  20.  Plus Minus Button
  21. jQuery scroll Nav

  

/*--------------------------------
[ End table content ]
-----------------------------------*/


(function($) {
    'use strict';


/*-------------------------------------------
  01. jQuery MeanMenu
--------------------------------------------- */
    
$('.mobile-menu nav').meanmenu({
    meanMenuContainer: '.mobile-menu-area',
    meanScreenWidth: "991",
    meanRevealPosition: "right",
});

/*-------------------------------------------
  02. wow js active
--------------------------------------------- */
  new WOW().init();
    
    
/*-------------------------------------------
  03. Product  Masonry (width)
--------------------------------------------- */ 
$('.htc__product__container').imagesLoaded( function() {
  
    // filter items on button click
    $('.product__menu').on( 'click', 'button', function() {
      var filterValue = $(this).attr('data-filter');
      $grid.isotope({ filter: filterValue });
    }); 
    // init Isotope
    var $grid = $('.product__list').isotope({
      itemSelector: '.single__pro',
      percentPosition: true,
      transitionDuration: '0.7s',
      masonry: {
        // use outer width of grid-sizer for columnWidth
        columnWidth: '.single__pro',
      }
    });

});

$('.product__menu button').on('click', function(event) {
    $(this).siblings('.is-checked').removeClass('is-checked');
    $(this).addClass('is-checked');
    event.preventDefault();
});



/*-------------------------------------------
  04. Sticky Header
--------------------------------------------- */ 
  var win = $(window);
  var sticky_id = $("#sticky-header-with-topbar");
  win.on('scroll',function() {    
    var scroll = win.scrollTop();
    if (scroll < 245) {
      sticky_id.removeClass("scroll-header");
    }else{
      sticky_id.addClass("scroll-header");
    }
  });
    
    
/*--------------------------
  05. ScrollUp
---------------------------- */
$.scrollUp({
    scrollText: '<i class="zmdi zmdi-chevron-up"></i>',
    easingType: 'linear',
    scrollSpeed: 900,
    animation: 'fade'
});
    
    
/*---------------------------
  06. Tooltip
------------------------------*/    
$('[data-toggle="tooltip"]').tooltip({
    animated: 'fade',
    placement: 'top',
    container: 'body'
});
    
    
/*-----------------------------------
  07. ScrollReveal Js Init
-------------------------------------- */
    window.sr = ScrollReveal({ duration: 800 , reset: true });
    sr.reveal('.foo');
    sr.reveal('.bar');
    
    
/*-------------------------------------------------------
  08. Fixed Footer bottom script ( Newsletter )
--------------------------------------------------------*/

var $newsletter_height = $(".htc__foooter__area");
$('.fixed__footer').css({'margin-bottom': $newsletter_height.height() + 'px'});


/*------------------------------------    
  09. Search Bar
--------------------------------------*/ 
    
  $( '.search__open' ).on( 'click', function () {
    $( 'body' ).toggleClass( 'search__box__show__hide' );
    return false;
  });

  $( '.search__close__btn .search__close__btn_icon' ).on( 'click', function () {
    $( 'body' ).toggleClass( 'search__box__show__hide' );
    return false;
  });
    
    
/*------------------------------------    
  10. Toogle Menu
--------------------------------------*/
  $('.toggle__menu').on('click', function() {
    $('.offsetmenu').addClass('offsetmenu__on');
    $('.body__overlay').addClass('is-visible');

  });

  $('.offsetmenu__close__btn').on('click', function() {
      $('.offsetmenu').removeClass('offsetmenu__on');
      $('.body__overlay').removeClass('is-visible');
  });

/*------------------------------------    
  11. Shopping Cart Area
--------------------------------------*/

  $('.cart__menu').on('click', function() {
    $('.shopping__cart').addClass('shopping__cart__on');
    $('.body__overlay').addClass('is-visible');

  });

  $('.offsetmenu__close__btn').on('click', function() {
      $('.shopping__cart').removeClass('shopping__cart__on');
      $('.body__overlay').removeClass('is-visible');
  });


/*------------------------------------    
  12. Filter Area
--------------------------------------*/

  $('.filter__menu').on('click', function() {
    $('.filter__wrap').addClass('filter__menu__on');
    $('.body__overlay').addClass('is-visible');

  });

  $('.filter__menu__close__btn').on('click', function() {
      $('.filter__wrap').removeClass('filter__menu__on');
      $('.body__overlay').removeClass('is-visible');
  });
    
    
/*------------------------------------    
  13. User Menu
--------------------------------------*/

  $('.user__menu').on('click', function() {
    $('.user__meta').addClass('user__meta__on');
    $('.body__overlay').addClass('is-visible');

  });
    
  $('.offsetmenu__close__btn').on('click', function() {
      $('.user__meta').removeClass('user__meta__on');
      $('.body__overlay').removeClass('is-visible');
  });



/*------------------------------------    
  14. Overlay Close
--------------------------------------*/
  $('.body__overlay').on('click', function() {
    $(this).removeClass('is-visible');
    $('.offsetmenu').removeClass('offsetmenu__on');
    $('.shopping__cart').removeClass('shopping__cart__on');
    $('.filter__wrap').removeClass('filter__menu__on');
    $('.user__meta').removeClass('user__meta__on');
  });

    
/*-----------------------------------------------
  15. Home Slider
-------------------------------------------------*/
  if ($('.slider__activation__wrap').length) {
    $('.slider__activation__wrap').owlCarousel({
      loop: true,
      margin:0,
      nav:true,
      autoplay: false,
      navText: [ '<i class="zmdi zmdi-chevron-left"></i>', '<i class="zmdi zmdi-chevron-right"></i>' ],
      autoplayTimeout: 10000,
      items:1,
      dots: false,
      lazyLoad: true,
      responsive:{
        0:{
          items:1
        },
        600:{
          items:1
        },
        800:{
          items:1
        },
        1024:{
          items:1
        },
        1200:{
          items:1
        },
        1400:{
          items:1
        },
        1920:{
          items:1
        }
      }
    });
  }

/*-----------------------------------------------
  16. Popular Product Wrap
-------------------------------------------------*/
  $('.popular__product__wrap').owlCarousel({
      loop: true,
      margin:0,
      nav:true,
      autoplay: false,
      navText: [ '<i class="zmdi zmdi-chevron-left"></i>', '<i class="zmdi zmdi-chevron-right"></i>' ],
      autoplayTimeout: 10000,
      items:3,
      dots: false,
      lazyLoad: true,
      responsive:{
        0:{
          items:1
        },
        600:{
          items:2
        },
        800:{
          items:2
        },
        1024:{
          items:3
        },
        1200:{
          items:3
        },
        1400:{
          items:3
        },
        1920:{
          items:3
        }
      }
    });
    
    
/*-----------------------------------------------
  17.  product-slider-active
-------------------------------------------------*/
  $('.single-portfolio-slider').owlCarousel({
      loop: true,
      nav:true,
      navText: [ '<i class="zmdi zmdi-chevron-left"></i>', '<i class="zmdi zmdi-chevron-right"></i>' ],
      items:1,
      responsive:{
        0:{
          items:1
        },
        600:{
          items:1
        },
        800:{
          items:1
        },
        1024:{
          items:1
        },
        1200:{
          items:1
        },
        1400:{
          items:1
        },
        1920:{
          items:1
        }
      }
    });


/*-----------------------------------------------
  17.  product-slider-active
-------------------------------------------------*/


  $('.product-slider-active').owlCarousel({
      loop: true,
      margin:0,
      nav:true,
      navText: [ '<i class="zmdi zmdi-chevron-left"></i>', '<i class="zmdi zmdi-chevron-right"></i>' ],
      items:3,
      responsive:{
        0:{
          items:1
        },
        600:{
          items:2
        },
        800:{
          items:2
        },
        1024:{
          items:3
        },
        1200:{
          items:3
        },
        1400:{
          items:3
        },
        1920:{
          items:3
        }
      }
    });


/*-----------------------------------------------
  17.  product-details-slider
-------------------------------------------------*/


  $('.product-details-slider').owlCarousel({
      loop: true,
      margin:20,
      nav:true,
      navText: [ '<i class="zmdi zmdi-chevron-left"></i>', '<i class="zmdi zmdi-chevron-right"></i>' ],
      items:3,
      responsive:{
        0:{
          items:1
        },
        600:{
          items:2
        },
        800:{
          items:2
        },
        1024:{
          items:3
        },
        1200:{
          items:3
        },
        1400:{
          items:3
        },
        1920:{
          items:3
        }
      }
    });


/*-----------------------------------------------
  18.  portfolio-slider-active
-------------------------------------------------*/


  $('.portfolio-slider-active').owlCarousel({
      loop: true,
      dotsEach: 1,
      nav:false,
      items:3,
      responsive:{
        0:{
          items:1
        },
        600:{
          items:2
        },
        800:{
          items:2
        },
        1024:{
          items:3
        },
        1200:{
          items:3
        },
        1400:{
          items:3
        },
        1920:{
          items:3
        }
      }
    });



/*-----------------------------------------------
  17. Testimonial Wrap
-------------------------------------------------*/


  $('.testimonial__wrap').owlCarousel({
      loop: true,
      margin:0,
      nav:false,
      autoplay: false,
      navText: false,
      autoplayTimeout: 10000,
      items:1,
      dots: false,
      lazyLoad: true,
      responsive:{
        0:{
          items:1
        },
        600:{
          items:1
        },
        800:{
          items:1
        },
        1024:{
          items:1
        },
        1200:{
          items:1
        },
        1400:{
          items:1
        },
        1920:{
          items:1
        }
      }
    });




/*--------------------------------
  18. Magnific Popup
----------------------------------*/

$('.video-popup').magnificPopup({
  type: 'iframe',
  mainClass: 'mfp-fade',
  removalDelay: 160,
  preloader: false,
  zoom: {
      enabled: true,
  }
});

$('.image-popup').magnificPopup({
  type: 'image',
  mainClass: 'mfp-fade',
  removalDelay: 100,
  gallery:{
      enabled:true, 
  }
});


/*-------------------------------
  19. Price Slider Active
--------------------------------*/
  $("#slider-range").slider({
      range: true,
      min: 10,
      max: 500,
      values: [110, 400],
      slide: function(event, ui) {
          $("#amount").val("$" + ui.values[0] + " - $" + ui.values[1]);
      }
  });
  $("#amount").val("$" + $("#slider-range").slider("values", 0) +
      " - $" + $("#slider-range").slider("values", 1));


/*-------------------------------
  20.  Plus Minus Button 
--------------------------------*/

    $(".cart-plus-minus").append('<div class="dec qtybutton">-</i></div><div class="inc qtybutton">+</div>');

    $(".qtybutton").on("click", function () {
        var $button = $(this);
        var oldValue = $button.parent().find("input").val();
        if ($button.text() == "+") {
            var newVal = parseFloat(oldValue) + 1;
        } else {
            // Don't allow decrementing below zero
            if (oldValue > 1) {
                var newVal = parseFloat(oldValue) - 1;
            } else {
                newVal = 1;
            }
        }
        $button.parent().find("input").val(newVal);
    });


/*--------------------------
  21. jQuery scroll Nav
---------------------------- */
    $('.onepage--menu').onePageNav({
        scrollOffset: 0
    }); 



/*---------------------
    countdown
  --------------------- */
    $('[data-countdown]').each(function() {
		var $this = $(this), finalDate = $(this).data('countdown');
		$this.countdown(finalDate, function(event) {
		$this.html(event.strftime('<span class="cdown day">%-D <p>Days</p></span> <span class="cdown hour">%-H <p>Hour</p></span> <span class="cdown minutes">%M <p>Min</p></span class="cdown second"> <span>%S <p>Sec</p></span>'));
		});
    });    
    
    
/* isotop active */
    var $grid = $('.grid');
    var $gridJustified = $('.grid-justified');
    var $gridItems = '.grid-item';
    // filter items on button click
    $grid.imagesLoaded(function() {
        
        $('.portfolio-menu-active').on('click', 'button', function() {
            $(this).siblings('.active').removeClass('active');
            $(this).addClass('active');
            var filterValue = $(this).attr('data-filter');
            $grid.isotope({
                filter: filterValue
            });
        });
        
        // init Isotope
        $grid.isotope({
            itemSelector: $gridItems,
            percentPosition: true,
            masonry: {
                // use outer width of grid-sizer for columnWidth
                columnWidth: $gridItems,
            }
        });
        
        // init Isotope
        $gridJustified.isotope({
            itemSelector: $gridItems,
            percentPosition: true,
            layoutMode: 'fitRows',
            masonry: {
                // use outer width of grid-sizer for columnWidth
                columnWidth: 1,
            }
        });
    });
    
    
    /*--
    Magnific Popup
    ------------------------*/
    $('.img-poppu').magnificPopup({
        type: 'image',
        gallery:{
            enabled:true
        }
    });
    
    
    $('.sidebar-active').stickySidebar({
        topSpacing: 80,
        bottomSpacing: 30,
        minWidth: 767,
    });


/*----------------------------------------------------------------
    Block Filters (мой)
--------------------------------------------------------------- */

    // -----------------------------------------------------------
    // Filter by subcategories

    $('#form-filters').click(function () {

        let new_link_all = ''
        var allElements = $(".subs_ids").toArray();

        let new_link = ''
        let checkbox_list = $('.checkbox-subcategory:checked').toArray()
        console.log(checkbox_list)

        if (checkbox_list.length > 0){
            let list_of_ids = checkbox_list.map(el => el.id.replace('sub', 'sub='))

            new_link = '?' + list_of_ids.join('&')
            let href_link = $('#subcategory-filter-btn').attr('href')

            $('#subcategory-filter-btn').attr('href', new_link)
        }else{
            allElements = allElements.map(el => el.id.replace('sub', 'sub='))
            new_link_all = '?' + allElements.join('&')

            let href_link = $('#subcategory-filter-btn').attr('href')
            $('#subcategory-filter-btn').attr('href', new_link_all)
        }
    })

    // -----------------------------------------------------------
    // Filter by price

    $('#price_filtered').click(function () {
        let price = $('#amount').val();

        var numberPattern = /\d+/g;
        let price_arr = price.match( numberPattern )

        price_arr[0] = ('price=' + price_arr[0])
        price_arr[1] = ('price=' + price_arr[1])
        console.log('+txt', price_arr)

        let new_link_price = '?' + price_arr.join('&')
        console.log('new link', new_link_price)

        $('#a-click').attr('href', new_link_price)

    });

    // -----------------------------------------------------------
    // Filter by Color#

    $('#color-ul').click(function () {

        let new_link_all = ''
        let new_link = ''

        var allElements = $(".color-a").toArray();
        let checkbox_list = $('.color-a:checked').toArray()
        console.log('checked', checkbox_list)
        console.log(allElements)
        if (checkbox_list.length > 0){
            checkbox_list = checkbox_list.map(el => el.id.replace('-', '='))

            new_link = '?' + checkbox_list.join('&')
            let href_link = $('#color-filter-btn').attr('href')
            $('#color-filter-btn').attr('href', new_link)
        }else{
            allElements = allElements.map(el => el.id.replace('-', '='))
            new_link_all = '?' + allElements.join('&')

            let href_link = $('#color-filter-btn').attr('href')
            $('#color-filter-btn').attr('href', new_link_all)
        }
    });

    // -----------------------------------------------------------
    // Login

    $('#log_btn').click(function () {
        let _login = $('#login_field').val();
        let _password = $('#password_field').val();
        $.ajax({
            url: '/ajax_log_passwd',
            data: {password_field:_password, login_field:_login},
            success: function(result){
                if (result.message_user === 'ok'){
                    $('.form-group').attr( 'onsubmit', 'return true');
                    alert('Welcome!');
                }else{
                    alert('Error');
                }
            }
        })
    })
    //----------------------------------------------------------------
    // Register

    let valid_login = false;
    let valid_email = false;
    let valid_passwd = false;
    let valid_passwd_confirm = false;

    let loginExp = /^[a-zA-Z0-9][a-zA-Z0-9_]{4,14}$/;
    let regExp_email = /^([a-z0-9_-]+\.)*[a-z0-9_-]+@[a-z0-9_-]+(\.[a-z0-9_-]+)*\.[a-z]{2,6}$/;
    let regExp_passwd = /(?=.*[0-9])(?=.*[a-z])(?=.*[A-Z])[0-9a-zA-Z*]{8,}/

    //----------------------------------------------------------------
    $('#login_field_reg').change(function () {
        let _login = $(this).val()

        if (!loginExp.test(_login)){
            $('#login_error_reg').text('Длина должна быть 5-15 и состоять из букв и цифр')
            valid_login = false;
        }else{
            $.ajax({
                url: '/ajax_reg',
                data: 'login_field=' + _login,
                success: function(result){
                    if (result.message_login === 'занят'){

                        $('#login_error').text('Логин уже занят')
                        valid_login = false;
                    }else{

                        $('#login_error').text('')
                        valid_login = true;
                    }
                }
            })
        }
    })
    $('#login_field_reg').focus(function () {

        $('#login_error').text('')
    })
    //----------------------------------------------------------------
    $('#email_field_reg').blur(function () {
        let _email = $(this).val()
        if (regExp_email.test(_email)){

            $('#email_error').text('')
            valid_email = true;
        }else{

            $('#email_error').text('Не валидный email')
            valid_email = false;
        }
    })
    $('#email_field_reg').focus(function () {

        $('#email_error').text('')
    })

    //----------------------------------------------------------------
    $('#password_field_reg').blur(function () {
        let _password = $(this).val()

        if (regExp_passwd.test(_password)){

            $('#password_error').text('')
            valid_passwd = true;
        }else{

            $('#password_error').text('Должно быть не менее 8 символов, цифра, буква в верхнем и нижнем регистре')
            valid_passwd = false;
        }
    })
    $('#password_field_reg').focus(function () {

        $('#password_error').text('')
    })

    //----------------------------------------------------------------
    $('#password_confirmation_field').blur(function () {
        let _password_confirm = $(this).val()

        if (_password_confirm === $('#password_field_reg').val()){
            $('#password_confirm_error').text('')
            valid_passwd_confirm = true;
        }else{

            $('#password_confirm_error').text('Должен соответствовать паролю, введённому в предыдущем поле')
            valid_passwd_confirm = false;
        }
    })
    $('#password_confirmation_field').focus(function () {
        $('#password_confirm_error').text('')
    })

    //----------------------------------------------------------------

    $('#submit_reg').click(function () {
        if (
            valid_login === true &&
            valid_email === true &&
            valid_passwd === true &&
            valid_passwd_confirm === true
        ){
            $('.form-group').attr( 'onsubmit', 'return true')
        }
    })
    //----------------------------------------------------------------




})(jQuery);





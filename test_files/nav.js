
jQuery(function(){
	// covers mouseenter/mouseleave events
	// (hover states, flyouts, etc.)
	// works in conjunction with CSS :hover pseudoclass

	// nav items
	// do not change order
	var sections = ["account","help","listen-online","programming","try-siriusxm","subscriptions","shop"];

	// menu behavior
	jQuery.each(jQuery(".primary-item, .secondary-item"), function(i) {
		
		var _this = this,
			section = sectionsGN[i],
			sectionType = jQuery(this).hasClass("primary-item")?"primary":"secondary",
			timeout;

		// handle hover over primary/secondary nav links
	
		jQuery("."+sectionType+"-item-"+section+" a.has-dropdown")
			.bind("click",function(e){
				if($(this).attr("href") === "#") {
					e.preventDefault();
				}
			})
			.bind("mouseenter focus", function(){
				var $this = jQuery(this);

				// reset hover states
				jQuery(".item-title").not(".primary-item-listen .primary-item-title").removeClass("active");

				jQuery(".primary-submenu-flyout, .secondary-submenu-flyout").hide();

				// persist hover state when entering flyout
				$this.addClass("active");

				// show flyout
				jQuery("."+sectionType+"-submenu-"+section).show().attr("aria-hidden", "false");

			});
			
		jQuery("."+sectionType+"-item-"+section+" a.item-title:not(.has-dropdown), .primary-nav a.logo")
			.bind("focus", function() {
				// reset hover states
				jQuery(".item-title").not(".primary-item-listen .primary-item-title").removeClass("active");

				jQuery(".primary-submenu-flyout, .secondary-submenu-flyout").hide();
			});

		// handle mouse out of links, flyouts
		jQuery("."+sectionType+"-item-"+section)
			.bind("mouseleave",function(){

				var $this = jQuery(this);

				// delay reduces flicker
				timeout = setTimeout(function(){

					$this.children(".item-title").removeClass("active");

					jQuery("."+sectionType+"-submenu-"+section).hide().attr("aria-hidden", "true");

				}, 200);

			})
			.bind("mouseenter",function(){
				clearTimeout(timeout);
			});
	});


	// search
	jQuery(".primary-item-search a.item-title").bind("click",function(e){
		e.preventDefault();
		e.stopPropagation();

		var $parent = jQuery(this).parent(".primary-item-search");

		if ($parent.hasClass("active")) {

			$parent.removeClass("active");
			jQuery("#search-query").hide();

		} else {

			$parent.addClass("active");
			jQuery("#search-query").show().focus();

		}

	});

    // mobile nav

    jQuery(".menu-icon").bind("click",function(e){
	    e.preventDefault();
	    e.stopPropagation();
		
		var menuIcon = jQuery(this),
			mobileNavDrawer = jQuery(".mobile-nav-drawer");
		
		if(menuIcon.hasClass("on")) {
			menuIcon.removeClass("on");
			menuIcon.css({ position: "", "z-index": "", "right": "", "top": "" });
			mobileNavDrawer.animate({ left: "-100%" });
		} else {
			menuIcon.addClass("on");
			menuIcon.css({ "position": "fixed", "z-index": 1001, "right": "100%", "top": "0px" }).animate({ "right": "10px" });
			mobileNavDrawer.animate({ left: "0px" });
		}
    });

		jQuery(window).resize(function() {
			var win = jQuery(this);

			if(win.width() >= 768) {
				jQuery(".menu-icon").removeClass("on");
				jQuery("body").animate({ left: 0 });
			}
		});

});

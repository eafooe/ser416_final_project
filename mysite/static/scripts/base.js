
        document.addEventListener("DOMContentLoaded", function(event) { 
            if (sessionStorage.getItem('sidebar-collapsed') && sessionStorage.getItem('sidebar-collapsed') == 'true'){
                console.log("Found that the sidebar should be collapsed");
                SidebarCollapse();
               
            } else {
                console.log("Found that the sidebar should not be collapsed");
            }
          });
        
          $(document).ready(function () {
            document.getElementsByTagName("html")[0].style.visibility = "visible";
            setTimeout(function(){
                document.getElementsByTagName("html")[0].style.visibility = "visible";
            }, 100);
        });

        // Hide submenus
        $('#body-row .collapse').collapse('hide');

        // Collapse/Expand icon
        $('#collapse-icon').addClass('fa-angle-double-left');

        // When you click on the hamburger menu, toggle the sidebar
        $('[data-toggle=toggle-sidebar]').click(function () {
            
            SidebarCollapse();
        });

        function SidebarCollapse() {
            $('.menu-collapsed').toggleClass('d-none');
            $('.submenu-icon').toggleClass('d-none');
            $('span.menu-icon').toggleClass('mr-3');
            $('#sidebar-container').toggleClass('sidebar-expanded sidebar-collapsed');

             // Treating d-flex/d-none on separators with title
    var SeparatorTitle = $('.sidebar-separator-title');
    if ( SeparatorTitle.hasClass('d-flex') ) {
        SeparatorTitle.removeClass('d-flex');
    } else {
        SeparatorTitle.addClass('d-flex');
    }
    
            // menu is collapse
            if ($('span.menu-icon').hasClass('mr-3')){
               sessionStorage.setItem('sidebar-collapsed', 'false');
            } else {
                sessionStorage.setItem('sidebar-collapsed', 'true');
            }
            
        }
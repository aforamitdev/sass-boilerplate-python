import os
folders=['abstracts','base','components','layout',"pages",'themes','vendors'];
#folders  in 7-1 pattens 
abstractfiles=['_animations.scss','_mixins.scss','_variables.scss','_phaceholder.scss'];

base=['_reset.scss','_typology.scss'];

components=['_buttons.scss','_carousel.scss','_cover.scss','_dropdown.scss'];

layout=['_navigation.scss','_grid.scss','_header.scss','_footer.scss','_sidebar.scss','_forms.scss']

pages=['_home.scss','_contact.scss'];

themes=['_theme.scss','_admin.scss']

vendors=['_bootstrap.scss','_jquery.scss'];

#to create all folder from folder list 
for folder in folders:
    os.makedirs('sass/'+folder)
    
#to create abstracts files inside folder abstracts 
for files in abstractfiles:
    open('sass/abstracts/'+files,"w")

for files in base:
    open('sass/base/'+files,"w")

for files in components:
    open('sass/components/'+files,"w")

for files in layout:
    open('sass/layout/'+files,"w")

for files in pages:
    open('sass/pages/'+files,"w")
for files in vendors:
    open('sass/vendors/'+files,"w")
for files in themes:
    open('sass/themes/'+files,"w")
    
f= open("sass/main.scss","w")
f.write("@import 'abstracts/animations';\n@import 'abstracts/mixins';\n  @import 'abstracts/variables';\n  @import 'abstracts/phaceholder';\n@import 'components/buttons';\n@import 'components/carousel';\n@import 'components/cover';\n@import 'components/dropdown';\n@import 'layout/navigation';\n@import 'layout/grid';\n@import 'layout/header';\n@import 'layout/footer';\n@import 'layout/sidebar';\n@import 'layout/forms';\n@import 'pages/home';\n@import 'pages/contact';\n@import 'themes/theme';\n")
f.close()

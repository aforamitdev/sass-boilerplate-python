import os
folders=['abstracts','base','components','layout',"pages",'themes','vendors'];
#folders  in 7-1 pattens 
abstractfiles=['_animations.scss','_mixins.scss','_variables.scss','_phaceholder.scss'];

base=['_reset.scss','_typology.scss'];

components=['_buttons.scss','_carousel.scss','_cover.scss','_dropdown.scss'];

layout=['_navigation.scss','_grid.scss','header.scss','_footer.scss','_sidebar.scss','forms.scss']

pages=['_home.scss','contact.scss'];

themes=['_theme.scss','_admin.scss']

vendors=['_bootstrap.scss','_jquery.scss'];

#to create all folder from folder list 
for folder in folders:
    os.makedirs('/sass/'+folder)
    
#to create abstracts files inside folder abstracts 
for files in abstractfiles:
    open('/sass/abstracts/'+files,"w")

for files in base:
    open('/sass/base/'+files,"w")

for files in components:
    open('/sass/components/'+files,"w")

for files in layout:
    open('/sass/layout/'+files,"w")

for files in pages:
    open('/sass/pages/'+files,"w")
for files in vendors:
    open('/sass/vendors/'+files,"w")
for files in themes:
    open('/sass/themes/'+files,"w")
    
f= open("/sass/main.scss","w")
f.write("@import 'abstracts/animations.scss'\n@import 'abstracts/mixins.scss'\n  @import 'abstracts/variables.scss'\n  @import 'abstracts/phaceholder.scss'\n@import 'components/buttons.scss'\n@import 'components/carousel.scss'\n@import 'components/cove.scss'\n@import 'components/dropdown.scss'\n@import 'layout/navigarion.scss'\n@import 'layout/grid.scss'\n@import 'layout/header.scss'\n@import 'layout/footer.scss'\n@import 'layout/sidebar.scss'\n@import 'layout/form.scss'\n@import 'pages/home.scss'\n@import 'pages/contact.scss'\n@import 'themes/theme.scss'\n")
f.close()

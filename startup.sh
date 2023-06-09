echo ">> FETCHING UPSTREAM..."
git clone https://github.com/LEGEND-AI/MUSICBOT /MUSICBOT
echo ">> INSTALLING REQUIREMENTS..."
cd /LEGEND-MUSIC
pip3 install -U -r requirements.txt
echo ">> STARTING MUSIC PLAYER USERBOT..."
clear
python3 runfile.py
echo "
#     #                        
##   ## #    #  ####  #  ####  
# # # # #    # #      # #    # 
#  #  # #    #  ####  # #      
#     # #    #      # # #      
#     # #    # #    # # #    # 
#     #  ####   ####  #  ####  
                                                                          
MUSIC PLAYER USERBOT IS SUCCESSFULLY DEPLOYED!
"

#1.Babes kopia gordeko dudan karpeta sortu
sudo mkdir /var/tmp/Backups/$(date +%F)

#2.Babes kopia inkrementala sortu, aurreko eguneko karpeta oraingo karpetarekin konparatuta, lehen sortutako karpetan gorde
sudo rsync -av --link-dest=/var/tmp/Backups/$(date -d yesterday +%F)/ /home/naiara/Segurtasuna/1.Laborategia/ /var/tmp/Backups/$(date +%F)

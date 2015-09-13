DIGAL="/usr/local/digital_alexandria"
if [ ! -d "$DIGAL" ]; then
	echo "Creating directory: $DIGAL"
	sudo mkdir -p $DIGAL
fi

sed --in-place=.bak '/digital_alexandria/d' ~/.zshrc
export PATH="$DIGAL:$PATH"
echo "export PATH=$DIGAL:$PATH" >> ~/.zshrc

sudo cp scripts/* $DIGAL
sudo chmod -R 755 $DIGAL


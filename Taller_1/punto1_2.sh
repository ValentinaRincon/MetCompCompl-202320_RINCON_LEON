input="indices_refraccion.csv"
while IFS=, read -r categoria _ nombre link; do
    if [ "$categoria" == "Categoria" ]; then
        continue
    fi
    mkdir -p "Descargas/$categoria"
    encoded_link=$(echo "$link" | sed 's/ /%20/g')
    curl -L "$encoded_link" -o "Descargas/$categoria/$nombre.yml"
done < "$input"
max=59
for i in $(seq -f %02g 4 $max)
do
    echo "Downloading and converting chapter: ${i}"
    wkhtmltopdf http://www.fictionalley.org/authors/bethany/LEAH${i}.html lily_evans_${i}.pdf
done

echo "Merging files to a single pdf"
gs -dBATCH -dNOPAUSE -q -sDEVICE=pdfwrite -sOutputFile=hogwarts_history.pdf lily_evans_*.pdf
rm -r lily_evans_*.pdf
echo "File generated successfully"

FILELIST=""
get_filelist(){
FILEDIR='dataset'
FILELIST=`find $FILEDIR -name "*.txt"`
}
get_filelist
#echo $FILELIST
for item in $FILELIST;do
    cat $item | sed s/"\t"/" "/g > $item
done

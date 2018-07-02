BASE="$HOME"
export PATH="$BASE/.anyenv/bin:$PATH"
eval "$(anyenv init -)"

for D in `\ls $BASE/.anyenv/envs`; do
    export PATH="$BASE/.anyenv/envs/$D/shims:$PATH"
done

function DJ()
{
    PARAMS="$@"; [ -n "$PARAMS" ] || PARAMS="shell";
    C=$PWD;
    while [ "$C" != / ]; do
        [ -f "$C/manage.py" ] && { python $C/manage.py $PARAMS ; break; };
        C=`dirname $C`
    done;
}

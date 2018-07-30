#!/bin/bash
export BDIR=${PWD}
export PDI_HOME="/opt/Pentaho/design-tools/data-integration"
ERROR=0

show_info(){
    echo ""
    echo "---------------------------------------------------------------------------"
    echo " Executing from: " $BDIR
    echo " PDI_HOME:       " $PDI_HOME
    echo " Add params:     " ${@:3}
    echo "---------------------------------------------------------------------------"
    echo ""
}
show_help(){
  echo ""
  echo "---------------------------------------------------------------------------"
  echo "# Usage:     etl.sh (job|trans) (path-to-file) (extra params)"
  echo "# PDI_HOME: " $PDI_HOME
  echo "---------------------------------------------------------------------------"
  echo ""
  exit 0;
}

# cd $PDI_HOME &&

if [ "x$1" = "xtrans" ]; then
  EXEC="pan"
elif [ "x$1" = "xjob" ]; then
  EXEC="kitchen"
else
  show_help
fi

if [ -z "$2" ]; then
    show_help
fi

FILE="$(cd "$(dirname "$2")"; pwd)/$(basename "$2")"
EXECSTR=./$EXEC".sh -file="$FILE" "${@:3}
echo "Executing "$EXECSTR

show_info
cd $PDI_HOME
. $EXECSTR

exit $ERROR

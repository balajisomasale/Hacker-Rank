read a 
read b 
read c 

if [[ $a -eq $b ]]; then
    if [[ $b -eq $c ]]; then
        echo EQUILATERAL
    
    elif [[ $b -ne $c ]]; then
        echo ISOSCELES
    fi
fi

if [[ $a -ne $b ]]; then
    if [[ $b -eq $c ]]; then
        echo ISOSCELES
    
    elif [[ $b -ne $c ]]; then
        echo SCALENE
    fi
fi

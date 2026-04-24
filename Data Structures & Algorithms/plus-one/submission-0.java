class Solution {
    public int[] plusOne(int[] digits) {
        if (digits[digits.length-1]!=9){
            digits[digits.length-1]+=1;
            return digits;
        }
        int i=digits.length-1;
        while(i>0 && digits[i]==9){

            digits[i]=0;
            i--;
        }
        digits[i]+=1;
        if(digits[i]==10){
            int[] result = new int[digits.length + 1];
            result[0]=1;
            return result;
            
            

        }
        return digits;
    }
}

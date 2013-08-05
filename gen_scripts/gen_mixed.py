@{
import inspect
import fileinput,os,string,re,sys
import time
from math import *
sys.path.append(".")
license_string = """////////////////////////////////////////////////////////////////////////////// 
// Copyright� 2013 by Broadcom Corporation. All Rights reserved.
// Original Author : Tony Kirke, Broadcom Corporation.
// This software is available under both the SystemC Open Source License 
// Version 3.1 and the MIT License
//
// The contents of this file are subject to the restrictions and limitations
// set forth in the SystemC Open Source License Version 3.1 (the "License").
// You may not use this file except in compliance with such restrictions and
// limitations. You may obtain instructions on how to receive a copy of the
// License at http://www.accellera.org/. Software distributed by Contributors
// under the License is distributed exclusively on an "AS IS" basis,
// WITHOUT WARRANTY OF ANY KIND, either express or implied.
// See the License for the specific language governing rights and limitations
// under the License.
////////////////////////////////////////////////////////////////////////////// 
// MIT License info:
// Permission is hereby granted, free of charge, to any person obtaining a copy 
// of this software and associated documentation files (the "Software"), to deal 
// in the Software without restriction, including without limitation the rights 
// to use, copy, modify, merge, publish, distribute, sublicense, and/or sell copies
// of the Software, and to permit persons to whom the Software is furnished to do so,
// subject to the following conditions:
//
// The above copyright notice and this permission notice shall be included in all 
// copies or substantial portions of the Software.
//
// THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, 
// EXPRESS OR IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF 
// MERCHANTABILITY, FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. 
// IN NO EVENT SHALL THE AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, 
// DAMAGES OR OTHER LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR 
// OTHERWISE, ARISING FROM, OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE 
// USE OR OTHER DEALINGS IN THE SOFTWARE.
//
////////////////////////////////////////////////////////////////////////////// 
"""

dbg_string = 'std::cout << "At line: " << __LINE__ << " " << __PRETTY_FUNCTION__ << "\\n";'

# Most Capitalize strings are Empy Variables

Namespace = 'sc_ft'
UNamespace = Namespace.upper()

GenDate = time.strftime("%Y/%m/%d")
Version = time.strftime("%Y%m%d")

# Most Capitalize strings are Empy Variables
Class = empy.args[0]
IClass = empy.args[1]
SClass = empy.args[2]
ISClass = empy.args[3]

UClass = Class.upper()
Header_inc = "SYSTEMC_"+UNamespace+"_"+UClass+"_"+Version+"_MIXED_FUNCTIONS_H_"

add_license_file = open("license.txt").read()

}@
// DO NOT EDIT THIS FILE IT WAS AUTOMATICALLY GENERATED @(GenDate)
@(add_license_file)
////////////////////////////////////////////////////////////////////////////// 
#ifndef @(Header_inc)
#define @(Header_inc)
namespace @(Namespace) {

// +
template <int T1, int I1, int T2, int I2, sc_q_mode QMODE, sc_q_mode QMODE1, sc_o_mode OMODE, sc_o_mode OMODE1> 
	@(Class)<
	Template_Max_Total_Bits<T1,I1,T2,I2>::maxval+2,
	Template_Max<I1,I2>::maxval+2,QMODE,OMODE> 
	operator +(const @(Class)<T1,I1,QMODE,OMODE>& a, 
			   const @(IClass)<T2,I2,QMODE1,OMODE1>& b) {
	
	@(Class)<
		Template_Max_Total_Bits<T1,I1,T2,I2>::maxval+2,
		Template_Max<I1,I2>::maxval+2,QMODE,OMODE> tmpa(a);
	@(Class)<
		Template_Max_Total_Bits<T1,I1,T2,I2>::maxval+2,
		Template_Max<I1,I2>::maxval+2,QMODE,OMODE> tmpb(b);
	tmpa.val += tmpb.getVal();
	return tmpa;
}
// +
template <int T1, int I1, int T2, int I2, sc_q_mode QMODE, sc_q_mode QMODE1, sc_o_mode OMODE, sc_o_mode OMODE1> 
	@(Class)<
	Template_Max_Total_Bits<T1,I1,T2,I2>::maxval+2,
	Template_Max<I1,I2>::maxval+2,QMODE,OMODE> 
	operator +(const @(IClass)<T1,I1,QMODE,OMODE>& a, 
			   const @(Class)<T2,I2,QMODE1,OMODE1>& b) {
	
	@(Class)<
		Template_Max_Total_Bits<T1,I1,T2,I2>::maxval+2,
		Template_Max<I1,I2>::maxval+2,QMODE,OMODE> tmpa(a);
	@(Class)<
		Template_Max_Total_Bits<T1,I1,T2,I2>::maxval+2,
		Template_Max<I1,I2>::maxval+2,QMODE,OMODE> tmpb(b);
	tmpa.val += tmpb.getVal();
	return tmpa;
}
// -
template <int T1, int I1, int T2, int I2, sc_q_mode QMODE, sc_q_mode QMODE1, sc_o_mode OMODE, sc_o_mode OMODE1> 
	@(Class)<
	Template_Max_Total_Bits<T1,I1,T2,I2>::maxval+2,
	Template_Max<I1,I2>::maxval+2,QMODE,OMODE> 
	operator -(const @(Class)<T1,I1,QMODE,OMODE>& a, 
			   const @(IClass)<T2,I2,QMODE1,OMODE1>& b) {
	
	@(Class)<
		Template_Max_Total_Bits<T1,I1,T2,I2>::maxval+2,
		Template_Max<I1,I2>::maxval+2,QMODE,OMODE> tmpa(a);
	@(Class)<
		Template_Max_Total_Bits<T1,I1,T2,I2>::maxval+2,
		Template_Max<I1,I2>::maxval+2,QMODE,OMODE> tmpb(b);

	tmpa.val -= tmpb.getVal();
	return tmpa;
}
// -
template <int T1, int I1, int T2, int I2, sc_q_mode QMODE, sc_q_mode QMODE1, sc_o_mode OMODE, sc_o_mode OMODE1> 
	@(Class)<
	Template_Max_Total_Bits<T1,I1,T2,I2>::maxval+2,
	Template_Max<I1,I2>::maxval+2,QMODE,OMODE> 
	operator -(const @(IClass)<T1,I1,QMODE,OMODE>& a, 
			   const @(Class)<T2,I2,QMODE1,OMODE1>& b) {
	
	@(Class)<
		Template_Max_Total_Bits<T1,I1,T2,I2>::maxval+2,
		Template_Max<I1,I2>::maxval+2,QMODE,OMODE> tmpa(a);
	@(Class)<
		Template_Max_Total_Bits<T1,I1,T2,I2>::maxval+2,
		Template_Max<I1,I2>::maxval+2,QMODE,OMODE> tmpb(b);

	tmpa.val -= tmpb.getVal();
	return tmpa;
}

// multiplication
template <int TOTAL_BITS_, int INT_BITS_, int TOTAL_BITS_1, int INT_BITS_1, sc_q_mode QMODE, sc_q_mode QMODE1, sc_o_mode OMODE, sc_o_mode OMODE1> 
	@(Class)<(TOTAL_BITS_+TOTAL_BITS_1),(INT_BITS_+INT_BITS_1),QMODE,OMODE> 
	operator *(const @(Class)<TOTAL_BITS_,INT_BITS_,QMODE,OMODE>& a, const @(IClass)<TOTAL_BITS_1,INT_BITS_1,QMODE1,OMODE1>& b) {
	
	@(Class)<(TOTAL_BITS_+TOTAL_BITS_1),(INT_BITS_+INT_BITS_1),QMODE,OMODE> tmp;
	typedef typename @(Class)<(TOTAL_BITS_+TOTAL_BITS_1),(INT_BITS_+INT_BITS_1),QMODE,OMODE>::val_type mult_val_type;
	// Don't need to saturate here!
	tmp.val = (mult_val_type)(a.getVal())*(mult_val_type)(b.getVal());
	return tmp;
}
// multiplication
template <int TOTAL_BITS_, int INT_BITS_, int TOTAL_BITS_1, int INT_BITS_1, sc_q_mode QMODE, sc_q_mode QMODE1, sc_o_mode OMODE, sc_o_mode OMODE1> 
	@(Class)<(TOTAL_BITS_+TOTAL_BITS_1),(INT_BITS_+INT_BITS_1),QMODE,OMODE> 
	operator *(const @(IClass)<TOTAL_BITS_,INT_BITS_,QMODE,OMODE>& a, const @(Class)<TOTAL_BITS_1,INT_BITS_1,QMODE1,OMODE1>& b) {
	
	@(Class)<(TOTAL_BITS_+TOTAL_BITS_1),(INT_BITS_+INT_BITS_1),QMODE,OMODE> tmp;
	typedef typename @(Class)<(TOTAL_BITS_+TOTAL_BITS_1),(INT_BITS_+INT_BITS_1),QMODE,OMODE>::val_type mult_val_type;
	// Don't need to saturate here!
	tmp.val = (mult_val_type)(a.getVal())*(mult_val_type)(b.getVal());
	return tmp;
}
 

// division
template <int TOTAL_BITS_, int INT_BITS_, int TOTAL_BITS_1, int INT_BITS_1, sc_q_mode QMODE, sc_q_mode QMODE1, sc_o_mode OMODE, sc_o_mode OMODE1> 
	@(Class)<(TOTAL_BITS_+TOTAL_BITS_1),(INT_BITS_+INT_BITS_1),QMODE,OMODE> 
	operator /(const @(Class)<TOTAL_BITS_,INT_BITS_,QMODE,OMODE>& a, const @(IClass)<TOTAL_BITS_1,INT_BITS_1,QMODE1,OMODE1>& b) {
	
	@(Class)<(TOTAL_BITS_+TOTAL_BITS_1),(INT_BITS_+INT_BITS_1),QMODE,OMODE> tmp;
	typedef typename @(Class)<(TOTAL_BITS_+TOTAL_BITS_1),(INT_BITS_+INT_BITS_1),QMODE,OMODE>::val_type mult_val_type;
	// Don't need to saturate here!
	tmp.val = (mult_val_type)(a.getVal())/(mult_val_type)(b.getVal());
	return tmp;
}
 


template <int TOTAL_BITS_, int INT_BITS_, int INT_BITS_1, sc_q_mode QMODE, sc_o_mode OMODE> 
	@(Class)<(TOTAL_BITS_+INT_BITS_1),(INT_BITS_+INT_BITS_1),QMODE,OMODE> 
	operator *(const @(IClass)<TOTAL_BITS_,INT_BITS_,QMODE,OMODE>& a, 
			   const @(SClass)<INT_BITS_1>& b) {
	
	@(Class)<(TOTAL_BITS_+INT_BITS_1),(INT_BITS_+INT_BITS_1),QMODE,OMODE> tmp;
	typedef typename @(Class)<(TOTAL_BITS_+INT_BITS_1),(INT_BITS_+INT_BITS_1),QMODE,OMODE>::val_type mult_val_type;
	tmp.val = (mult_val_type)(a.getVal())*(mult_val_type)b.to_int();
	return tmp;
}
template <int TOTAL_BITS_, int INT_BITS_, int INT_BITS_1, sc_q_mode QMODE, sc_o_mode OMODE> 
	@(Class)<(TOTAL_BITS_+INT_BITS_1),(INT_BITS_+INT_BITS_1),QMODE,OMODE> 
	operator *(const @(SClass)<INT_BITS_1>& b,
	           const @(IClass)<TOTAL_BITS_,INT_BITS_,QMODE,OMODE>& a) {
	@(Class)<(TOTAL_BITS_+INT_BITS_1),(INT_BITS_+INT_BITS_1),QMODE,OMODE> tmp;
	typedef typename @(Class)<(TOTAL_BITS_+INT_BITS_1),(INT_BITS_+INT_BITS_1),QMODE,OMODE>::val_type mult_val_type;
	tmp.val = (mult_val_type)(a.getVal())*(mult_val_type)b.to_int();
	return tmp;
}

template <int TOTAL_BITS_, int INT_BITS_, int INT_BITS_1, sc_q_mode QMODE, sc_o_mode OMODE> 
	@(Class)<(TOTAL_BITS_+INT_BITS_1),(INT_BITS_+INT_BITS_1),QMODE,OMODE> 
	 operator *(const @(SClass)<INT_BITS_1>& b,
				const @(Class)<TOTAL_BITS_,INT_BITS_,QMODE,OMODE>& a) {
	 
	 @(Class)<(TOTAL_BITS_+INT_BITS_1),(INT_BITS_+INT_BITS_1),QMODE,OMODE> tmp;
	 typedef typename @(Class)<(TOTAL_BITS_+INT_BITS_1),(INT_BITS_+INT_BITS_1),QMODE,OMODE>::val_type mult_val_type;
	 tmp.val = b*a.getVal();
	 return tmp;
}
 
template <int TOTAL_BITS_, int INT_BITS_, int INT_BITS_1, sc_q_mode QMODE, sc_o_mode OMODE> 
	@(Class)<(TOTAL_BITS_+INT_BITS_1),(INT_BITS_+INT_BITS_1),QMODE,OMODE> 
	 operator *(const @(Class)<TOTAL_BITS_,INT_BITS_,QMODE,OMODE>& a,
	            const @(SClass)<INT_BITS_1>& b) {
	 
	 @(Class)<(TOTAL_BITS_+INT_BITS_1),(INT_BITS_+INT_BITS_1),QMODE,OMODE> tmp;
	 typedef typename @(Class)<(TOTAL_BITS_+INT_BITS_1),(INT_BITS_+INT_BITS_1),QMODE,OMODE>::val_type mult_val_type;
	 tmp.val = b*a.getVal();
	 return tmp;
 }

 ///
 template <int TOTAL_BITS_, int INT_BITS_, int INT_BITS_1, sc_q_mode QMODE, sc_o_mode OMODE> 
	@(Class)<(TOTAL_BITS_+INT_BITS_1),(INT_BITS_+INT_BITS_1),QMODE,OMODE> 
	operator *(const @(IClass)<TOTAL_BITS_,INT_BITS_,QMODE,OMODE>& a, 
			   const @(ISClass)<INT_BITS_1>& b) {
	
	@(Class)<(TOTAL_BITS_+INT_BITS_1),(INT_BITS_+INT_BITS_1),QMODE,OMODE> tmp;
	typedef typename @(Class)<(TOTAL_BITS_+INT_BITS_1),(INT_BITS_+INT_BITS_1),QMODE,OMODE>::val_type mult_val_type;
	tmp.val = (mult_val_type)(a.getVal())*(mult_val_type)b.to_int();
	return tmp;
}
template <int TOTAL_BITS_, int INT_BITS_, int INT_BITS_1, sc_q_mode QMODE, sc_o_mode OMODE> 
	@(Class)<(TOTAL_BITS_+INT_BITS_1),(INT_BITS_+INT_BITS_1),QMODE,OMODE> 
	operator *(const @(ISClass)<INT_BITS_1>& b,
	           const @(IClass)<TOTAL_BITS_,INT_BITS_,QMODE,OMODE>& a) {
	@(Class)<(TOTAL_BITS_+INT_BITS_1),(INT_BITS_+INT_BITS_1),QMODE,OMODE> tmp;
	typedef typename @(Class)<(TOTAL_BITS_+INT_BITS_1),(INT_BITS_+INT_BITS_1),QMODE,OMODE>::val_type mult_val_type;
	tmp.val = (mult_val_type)(a.getVal())*(mult_val_type)b.to_int();
	return tmp;
}

template <int TOTAL_BITS_, int INT_BITS_, int INT_BITS_1, sc_q_mode QMODE, sc_o_mode OMODE> 
	@(Class)<(TOTAL_BITS_+INT_BITS_1),(INT_BITS_+INT_BITS_1),QMODE,OMODE> 
	 operator *(const @(ISClass)<INT_BITS_1>& b,
				const @(Class)<TOTAL_BITS_,INT_BITS_,QMODE,OMODE>& a) {
	 
	 @(Class)<(TOTAL_BITS_+INT_BITS_1),(INT_BITS_+INT_BITS_1),QMODE,OMODE> tmp;
	 typedef typename @(Class)<(TOTAL_BITS_+INT_BITS_1),(INT_BITS_+INT_BITS_1),QMODE,OMODE>::val_type mult_val_type;
	 tmp.val = b*a.getVal();
	 return tmp;
}
 
template <int TOTAL_BITS_, int INT_BITS_, int INT_BITS_1, sc_q_mode QMODE, sc_o_mode OMODE> 
	@(Class)<(TOTAL_BITS_+INT_BITS_1),(INT_BITS_+INT_BITS_1),QMODE,OMODE> 
	 operator *(const @(Class)<TOTAL_BITS_,INT_BITS_,QMODE,OMODE>& a,
	            const @(ISClass)<INT_BITS_1>& b) {
	 
	 @(Class)<(TOTAL_BITS_+INT_BITS_1),(INT_BITS_+INT_BITS_1),QMODE,OMODE> tmp;
	 typedef typename @(Class)<(TOTAL_BITS_+INT_BITS_1),(INT_BITS_+INT_BITS_1),QMODE,OMODE>::val_type mult_val_type;
	 tmp.val = b*a.getVal();
	 return tmp;
 }
 

// ^
template <int TOTAL_BITS_, int INT_BITS_, int TOTAL_BITS_1, int INT_BITS_1, sc_q_mode QMODE, sc_q_mode QMODE1, sc_o_mode OMODE, sc_o_mode OMODE1> 
	bool operator ==(const @(Class)<TOTAL_BITS_,INT_BITS_,QMODE,OMODE>& a, const @(IClass)<TOTAL_BITS_1,INT_BITS_1,QMODE1,OMODE1>& b) {
	@(Class)<Template_Max_Total_Bits<TOTAL_BITS_,INT_BITS_,TOTAL_BITS_1,INT_BITS_1>::maxval+2,Template_Max<INT_BITS_,INT_BITS_1>::maxval+2,QMODE,OMODE> tmpa(a);
	@(Class)<Template_Max_Total_Bits<TOTAL_BITS_,INT_BITS_,TOTAL_BITS_1,INT_BITS_1>::maxval+2,Template_Max<INT_BITS_,INT_BITS_1>::maxval+2,QMODE,OMODE> tmpb(b);
	return (tmpa.val == tmpb.val);
}
template <int TOTAL_BITS_, int INT_BITS_, int TOTAL_BITS_1, int INT_BITS_1, sc_q_mode QMODE, sc_q_mode QMODE1, sc_o_mode OMODE, sc_o_mode OMODE1> 
	bool operator ==(const @(IClass)<TOTAL_BITS_1,INT_BITS_1,QMODE1,OMODE1>& b, const @(Class)<TOTAL_BITS_,INT_BITS_,QMODE,OMODE>& a) {
    @(Class)<Template_Max_Total_Bits<TOTAL_BITS_,INT_BITS_,TOTAL_BITS_1,INT_BITS_1>::maxval+2,Template_Max<INT_BITS_,INT_BITS_1>::maxval+2,QMODE,OMODE> tmpa(a);
	@(Class)<Template_Max_Total_Bits<TOTAL_BITS_,INT_BITS_,TOTAL_BITS_1,INT_BITS_1>::maxval+2,Template_Max<INT_BITS_,INT_BITS_1>::maxval+2,QMODE,OMODE> tmpb(b);
	return (tmpa.val == tmpb.val);
}
template <int TOTAL_BITS_, int INT_BITS_, int TOTAL_BITS_1, int INT_BITS_1, sc_q_mode QMODE, sc_q_mode QMODE1, sc_o_mode OMODE, sc_o_mode OMODE1> 
	bool operator <(const @(Class)<TOTAL_BITS_,INT_BITS_,QMODE,OMODE>& a, const @(IClass)<TOTAL_BITS_1,INT_BITS_1,QMODE1,OMODE1>& b) {
	    @(Class)<Template_Max_Total_Bits<TOTAL_BITS_,INT_BITS_,TOTAL_BITS_1,INT_BITS_1>::maxval+2,Template_Max<INT_BITS_,INT_BITS_1>::maxval+2,QMODE,OMODE> tmpa(a);
	    @(Class)<Template_Max_Total_Bits<TOTAL_BITS_,INT_BITS_,TOTAL_BITS_1,INT_BITS_1>::maxval+2,Template_Max<INT_BITS_,INT_BITS_1>::maxval+2,QMODE,OMODE> tmpb(b);
		return (tmpa.val < tmpb.val);
}
template <int TOTAL_BITS_, int INT_BITS_, int TOTAL_BITS_1, int INT_BITS_1, sc_q_mode QMODE, sc_q_mode QMODE1, sc_o_mode OMODE, sc_o_mode OMODE1> 
	bool operator <(const @(IClass)<TOTAL_BITS_,INT_BITS_,QMODE,OMODE>& a, const @(Class)<TOTAL_BITS_1,INT_BITS_1,QMODE1,OMODE1>& b) {
	    @(Class)<Template_Max_Total_Bits<TOTAL_BITS_,INT_BITS_,TOTAL_BITS_1,INT_BITS_1>::maxval+2,Template_Max<INT_BITS_,INT_BITS_1>::maxval+2,QMODE,OMODE> tmpa(a);
	    @(Class)<Template_Max_Total_Bits<TOTAL_BITS_,INT_BITS_,TOTAL_BITS_1,INT_BITS_1>::maxval+2,Template_Max<INT_BITS_,INT_BITS_1>::maxval+2,QMODE,OMODE> tmpb(b);
		return (tmpa.val < tmpb.val);
}
// re-use previous operators
template <int TOTAL_BITS_, int INT_BITS_, int TOTAL_BITS_1, int INT_BITS_1, sc_q_mode QMODE, sc_q_mode QMODE1, sc_o_mode OMODE, sc_o_mode OMODE1> 
	bool operator !=(const @(Class)<TOTAL_BITS_,INT_BITS_,QMODE,OMODE>& a, const @(IClass)<TOTAL_BITS_1,INT_BITS_1,QMODE1,OMODE1>& b) {
	    @(Class)<Template_Max_Total_Bits<TOTAL_BITS_,INT_BITS_,TOTAL_BITS_1,INT_BITS_1>::maxval+2,Template_Max<INT_BITS_,INT_BITS_1>::maxval+2,QMODE,OMODE> tmpa(a);
	    @(Class)<Template_Max_Total_Bits<TOTAL_BITS_,INT_BITS_,TOTAL_BITS_1,INT_BITS_1>::maxval+2,Template_Max<INT_BITS_,INT_BITS_1>::maxval+2,QMODE,OMODE> tmpb(b);
		return !(tmpa.val == tmpb.val);
}
// re-use previous operators
template <int TOTAL_BITS_, int INT_BITS_, int TOTAL_BITS_1, int INT_BITS_1, sc_q_mode QMODE, sc_q_mode QMODE1, sc_o_mode OMODE, sc_o_mode OMODE1> 
	bool operator !=(const @(IClass)<TOTAL_BITS_,INT_BITS_,QMODE,OMODE>& a, const @(Class)<TOTAL_BITS_1,INT_BITS_1,QMODE1,OMODE1>& b) {
	    @(Class)<Template_Max_Total_Bits<TOTAL_BITS_,INT_BITS_,TOTAL_BITS_1,INT_BITS_1>::maxval+2,Template_Max<INT_BITS_,INT_BITS_1>::maxval+2,QMODE,OMODE> tmpa(a);
	    @(Class)<Template_Max_Total_Bits<TOTAL_BITS_,INT_BITS_,TOTAL_BITS_1,INT_BITS_1>::maxval+2,Template_Max<INT_BITS_,INT_BITS_1>::maxval+2,QMODE,OMODE> tmpb(b);
		return !(tmpa.val == tmpb.val);
}
template <int TOTAL_BITS_, int INT_BITS_, int TOTAL_BITS_1, int INT_BITS_1, sc_q_mode QMODE, sc_q_mode QMODE1, sc_o_mode OMODE, sc_o_mode OMODE1> 
	bool operator >(const @(Class)<TOTAL_BITS_,INT_BITS_,QMODE,OMODE>& a, const @(IClass)<TOTAL_BITS_1,INT_BITS_1,QMODE1,OMODE1>& b) {
	    @(Class)<Template_Max_Total_Bits<TOTAL_BITS_,INT_BITS_,TOTAL_BITS_1,INT_BITS_1>::maxval+2,Template_Max<INT_BITS_,INT_BITS_1>::maxval+2,QMODE,OMODE> tmpa(a);
	    @(Class)<Template_Max_Total_Bits<TOTAL_BITS_,INT_BITS_,TOTAL_BITS_1,INT_BITS_1>::maxval+2,Template_Max<INT_BITS_,INT_BITS_1>::maxval+2,QMODE,OMODE> tmpb(b);
		return (tmpb.val < tmpa.val);
}
template <int TOTAL_BITS_, int INT_BITS_, int TOTAL_BITS_1, int INT_BITS_1, sc_q_mode QMODE, sc_q_mode QMODE1, sc_o_mode OMODE, sc_o_mode OMODE1> 
	bool operator >(const @(IClass)<TOTAL_BITS_,INT_BITS_,QMODE,OMODE>& a, const @(Class)<TOTAL_BITS_1,INT_BITS_1,QMODE1,OMODE1>& b) {
	    @(Class)<Template_Max_Total_Bits<TOTAL_BITS_,INT_BITS_,TOTAL_BITS_1,INT_BITS_1>::maxval+2,Template_Max<INT_BITS_,INT_BITS_1>::maxval+2,QMODE,OMODE> tmpa(a);
	    @(Class)<Template_Max_Total_Bits<TOTAL_BITS_,INT_BITS_,TOTAL_BITS_1,INT_BITS_1>::maxval+2,Template_Max<INT_BITS_,INT_BITS_1>::maxval+2,QMODE,OMODE> tmpb(b);
		return (tmpb.val < tmpa.val);
}
template <int TOTAL_BITS_, int INT_BITS_, int TOTAL_BITS_1, int INT_BITS_1, sc_q_mode QMODE, sc_q_mode QMODE1, sc_o_mode OMODE, sc_o_mode OMODE1> 
	bool operator <=(const @(Class)<TOTAL_BITS_,INT_BITS_,QMODE,OMODE>& a, const @(IClass)<TOTAL_BITS_1,INT_BITS_1,QMODE1,OMODE1>& b) {
	    @(Class)<Template_Max_Total_Bits<TOTAL_BITS_,INT_BITS_,TOTAL_BITS_1,INT_BITS_1>::maxval+2,Template_Max<INT_BITS_,INT_BITS_1>::maxval+2,QMODE,OMODE> tmpa(a);
	    @(Class)<Template_Max_Total_Bits<TOTAL_BITS_,INT_BITS_,TOTAL_BITS_1,INT_BITS_1>::maxval+2,Template_Max<INT_BITS_,INT_BITS_1>::maxval+2,QMODE,OMODE> tmpb(b);
		return !(tmpb.val < tmpa.val);
}
template <int TOTAL_BITS_, int INT_BITS_, int TOTAL_BITS_1, int INT_BITS_1, sc_q_mode QMODE, sc_q_mode QMODE1, sc_o_mode OMODE, sc_o_mode OMODE1> 
	bool operator <=(const @(IClass)<TOTAL_BITS_,INT_BITS_,QMODE,OMODE>& a, const @(Class)<TOTAL_BITS_1,INT_BITS_1,QMODE1,OMODE1>& b) {
	    @(Class)<Template_Max_Total_Bits<TOTAL_BITS_,INT_BITS_,TOTAL_BITS_1,INT_BITS_1>::maxval+2,Template_Max<INT_BITS_,INT_BITS_1>::maxval+2,QMODE,OMODE> tmpa(a);
	    @(Class)<Template_Max_Total_Bits<TOTAL_BITS_,INT_BITS_,TOTAL_BITS_1,INT_BITS_1>::maxval+2,Template_Max<INT_BITS_,INT_BITS_1>::maxval+2,QMODE,OMODE> tmpb(b);
		return !(tmpb.val < tmpa.val);
}
template <int TOTAL_BITS_, int INT_BITS_, int TOTAL_BITS_1, int INT_BITS_1, sc_q_mode QMODE, sc_q_mode QMODE1, sc_o_mode OMODE, sc_o_mode OMODE1> 
	bool operator >=(const @(Class)<TOTAL_BITS_,INT_BITS_,QMODE,OMODE>& a, const @(IClass)<TOTAL_BITS_1,INT_BITS_1,QMODE1,OMODE1>& b) {
	    @(Class)<Template_Max_Total_Bits<TOTAL_BITS_,INT_BITS_,TOTAL_BITS_1,INT_BITS_1>::maxval+2,Template_Max<INT_BITS_,INT_BITS_1>::maxval+2,QMODE,OMODE> tmpa(a);
	    @(Class)<Template_Max_Total_Bits<TOTAL_BITS_,INT_BITS_,TOTAL_BITS_1,INT_BITS_1>::maxval+2,Template_Max<INT_BITS_,INT_BITS_1>::maxval+2,QMODE,OMODE> tmpb(b);
		return !(tmpa.val < tmpb.val);
}
template <int TOTAL_BITS_, int INT_BITS_, int TOTAL_BITS_1, int INT_BITS_1, sc_q_mode QMODE, sc_q_mode QMODE1, sc_o_mode OMODE, sc_o_mode OMODE1> 
	bool operator >=(const @(IClass)<TOTAL_BITS_,INT_BITS_,QMODE,OMODE>& a, const @(Class)<TOTAL_BITS_1,INT_BITS_1,QMODE1,OMODE1>& b) {
	    @(Class)<Template_Max_Total_Bits<TOTAL_BITS_,INT_BITS_,TOTAL_BITS_1,INT_BITS_1>::maxval+2,Template_Max<INT_BITS_,INT_BITS_1>::maxval+2,QMODE,OMODE> tmpa(a);
	    @(Class)<Template_Max_Total_Bits<TOTAL_BITS_,INT_BITS_,TOTAL_BITS_1,INT_BITS_1>::maxval+2,Template_Max<INT_BITS_,INT_BITS_1>::maxval+2,QMODE,OMODE> tmpb(b);
		return !(tmpa.val < tmpb.val);
}





} // end namespace @(Namespace)


#endif
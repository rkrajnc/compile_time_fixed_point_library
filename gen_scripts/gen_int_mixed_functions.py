@{
import inspect
import fileinput,os,string,re,sys
import time
from math import *
sys.path.append(".")
license_string = """////////////////////////////////////////////////////////////////////////////// 
// Copyrightę 2013 by Broadcom Corporation. All Rights reserved.
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

int_types = ['int8_t','int16_t','int32_t','int64_t','uint8_t','uint16_t','uint32_t','uint64_t']
base_types = ['int8_t','int16_t','int32_t','int64_t','uint8_t','uint16_t','uint32_t','uint64_t','double']

assign_form_types = ['double']
assign_form1_types = int_types
div_form_types = base_types

dbg_string = 'std::cout << "At line: " << __LINE__ << " " << __PRETTY_FUNCTION__ << "\\n";'
dbg_string = ' ';

Namespace = 'sc_ft'
UNamespace = Namespace.upper()

GenDate = time.strftime("%Y/%m/%d")
Version = time.strftime("%Y%m%d")

# Most Capitalize strings are Empy Variables
Class = empy.args[0]
IClass = empy.args[1]
UClass = Class.upper()

Header_inc = "SYSTEMC_"+UNamespace+"_"+UClass+"_"+Version+"_MIXED_FUNCTIONS_H_"

add_license_file = open("license.txt").read()

}@
// DO NOT EDIT THIS FILE IT WAS AUTOMATICALLY GENERATED ON @(GenDate)
@(add_license_file)
////////////////////////////////////////////////////////////////////////////// 

#ifndef @(Header_inc)
#define @(Header_inc)

namespace @(Namespace) {

// TEMPLATE functions for +,-,*,/ (divide returns double)
template <int W_,  int W_1>  @(Class)<Template_Max<W_,W_1+1>::maxval+1>
	operator +(const @(Class)<W_>& a, const @(IClass)<W_1>& b) {
	@(Class)<Template_Max<W_,W_1+1>::maxval+1> tmp(a);
	tmp += b;
	return(tmp);
}
template <int W_,  int W_1>  @(Class)<Template_Max<W_+1,W_1>::maxval+1>
	operator +(const @(IClass)<W_>& a, const @(Class)<W_1>& b) {
	@(Class)<Template_Max<W_+1,W_1>::maxval+1> tmp(a);
	tmp += b;
	return(tmp);
}

template <int W_,  int W_1>  @(Class)<Template_Max<W_,W_1+1>::maxval+1>
	operator -(const @(Class)<W_>& a, const @(IClass)<W_1>& b) {
	@(Class)<Template_Max<W_,W_1+1>::maxval+1> tmp(a);
	tmp -= b;
	return(tmp);
}
template <int W_,  int W_1>  @(Class)<Template_Max<W_+1,W_1>::maxval+1>
	operator -(const @(IClass)<W_>& a, const @(Class)<W_1>& b) {
	@(Class)<Template_Max<W_+1,W_1>::maxval+1> tmp(a);
	tmp -= b;
	return(tmp);
}

	
// multiplication
template <int W_, int W_1> @(Class)<W_+W_1> 
operator *(const @(Class)<W_>& a, const @(IClass)<W_1>& b) {
	 @(Class)<W_+W_1> tmp;
	 typedef typename @(Class)<W_+W_1>::val_type mult_val_type;
	 tmp.val = (mult_val_type)(a.getVal())*(mult_val_type)(b.getVal());
	 return tmp;
}
template <int W_, int W_1> @(Class)<W_+W_1> 
operator *(const @(IClass)<W_>& a, const @(Class)<W_1>& b) {
	 @(Class)<W_+W_1> tmp;
	 typedef typename @(Class)<W_+W_1>::val_type mult_val_type;
	 tmp.val = (mult_val_type)(a.getVal())*(mult_val_type)(b.getVal());
	 return tmp;
}
template <int W_, int W_1> @(Class)<W_+W_1> 
operator /(const @(IClass)<W_>& a, const @(Class)<W_1>& b) {
	 @(Class)<W_+W_1> tmp;
	 typedef typename @(Class)<W_+W_1>::val_type mult_val_type;
	 tmp.val = (mult_val_type)(a.getVal())/(mult_val_type)(b.getVal());
	 return tmp;
}  
template <int W_, int W_1> @(Class)<W_+W_1> 
operator /(const @(Class)<W_>& a, const @(IClass)<W_1>& b) {
	 @(Class)<W_+W_1> tmp;
	 typedef typename @(Class)<W_+W_1>::val_type mult_val_type;
	 tmp.val = (mult_val_type)(a.getVal())/(mult_val_type)(b.getVal());
	 return tmp;
}  

// <<
template <int W_,  int W_1>  @(Class)<W_+(1<<W_1)-1>
	operator <<(const @(Class)<W_>& a, const @(IClass)<W_1>& shift) {
	@(Class)<W_+(1<<W_1)-1> tmp(a);
	tmp <<= shift;
	return(tmp);
}
// Non-fixed bit-width type shifts
template <int W_, typename T_>  @(Class)<W_>
	operator <<(const @(Class)<W_>& a, const T_& shift) {
	@(Class)<W_> tmp(a);
	tmp <<= shift;
	return(tmp);
}
template <int W_, typename T_>  @(IClass)<W_>
	operator <<(const @(IClass)<W_>& a, const T_& shift) {
	@(IClass)<W_> tmp(a);
	tmp <<= shift;
	return(tmp);
}
// >>
template <int W_,  int W_1>  @(Class)<W_>
	operator >>(const @(Class)<W_>& a, const @(IClass)<W_1>& shift) {
	@(Class)<W_> tmp(a);
	tmp >>= shift;
	return(tmp);
}

template <int W_, typename T_>  @(Class)<W_>
	operator >>(const @(Class)<W_>& a, const T_& shift) {
	@(Class)<W_> tmp(a);
	tmp >>= shift;
	return(tmp);
}
template <int W_, typename T_>  @(IClass)<W_>
	operator >>(const @(IClass)<W_>& a, const T_& shift) {
	@(IClass)<W_> tmp(a);
	tmp >>= shift;
	return(tmp);
}



template <int W_,  int W_1>  @(Class)<Template_Max<W_,W_1>::maxval>
	operator |(const @(Class)<W_>& a, const @(IClass)<W_1>& b) {
	@(Class)<Template_Max<W_,W_1>::maxval> tmp(a);
	tmp |= b;
	return(tmp);
}
template <int W_,  int W_1>  @(Class)<Template_Max<W_,W_1>::maxval>
	operator |(const @(IClass)<W_>& a, const @(Class)<W_1>& b) {
	@(Class)<Template_Max<W_,W_1>::maxval> tmp(a);
	tmp |= b;
	return(tmp);
}

template <int W_,  int W_1>  @(Class)<Template_Max<W_,W_1>::maxval>
	operator &(const @(Class)<W_>& a, const @(IClass)<W_1>& b) {
	@(Class)<Template_Max<W_,W_1>::maxval> tmp(a);
	tmp &= b;
	return(tmp);
}
template <int W_,  int W_1>  @(Class)<Template_Max<W_,W_1>::maxval>
	operator &(const @(IClass)<W_>& a, const @(Class)<W_1>& b) {
	@(Class)<Template_Max<W_,W_1>::maxval> tmp(a);
	tmp &= b;
	return(tmp);
}

template <int W_,  int W_1>  @(Class)<Template_Max<W_,W_1>::maxval>
	operator ^(const @(Class)<W_>& a, const @(IClass)<W_1>& b) {
	@(Class)<Template_Max<W_,W_1>::maxval> tmp(a);
	tmp |= b;
	return(tmp);
}
template <int W_,  int W_1>  @(Class)<Template_Max<W_,W_1>::maxval>
	operator ^(const @(IClass)<W_>& a, const @(Class)<W_1>& b) {
	@(Class)<Template_Max<W_,W_1>::maxval> tmp(a);
	tmp |= b;
	return(tmp);
}


// Operations to support mixing with ints & doubles, etc

// Comparison operators "==,!=,<<=,>,>=" between this type and 'double'

// int with uint
template <int W_,  int W_1> bool operator ==(const @(Class)<W_>& a, const @(IClass)<W_1>& b) {
	@(Class)<Template_Max<W_,W_1>::maxval+1> tmpa(a);
	@(Class)<Template_Max<W_,W_1>::maxval+1> tmpb(b);
	return (tmpa.val == tmpb.val);
}

template <int W_,  int W_1> bool operator <(const @(Class)<W_>& a, const @(IClass)<W_1>& b) {
	@(Class)<Template_Max<W_,W_1>::maxval+1> tmpa(a);
	@(Class)<Template_Max<W_,W_1>::maxval+1> tmpb(b);
	return (tmpa.val < tmpb.val);
}

template <int W_,  int W_1> bool operator !=(const @(Class)<W_>& a, const @(IClass)<W_1>& b) {
	return !(a == b);
}
template <int W_,  int W_1> bool operator >(const @(Class)<W_>& a, const @(IClass)<W_1>& b) {
	return (b < a);
}
template <int W_,  int W_1> bool operator <=(const @(Class)<W_>& a, const @(IClass)<W_1>& b) {
	return !(b<a);
}
template <int W_,  int W_1> bool operator >=(const @(Class)<W_>& a, const @(IClass)<W_1>& b) {
	return !(a<b);
}
// uint with int
template <int W_,  int W_1> bool operator ==(const @(IClass)<W_>& a, const @(Class)<W_1>& b) {
	@(Class)<Template_Max<W_,W_1>::maxval+1> tmpa(a);
	@(Class)<Template_Max<W_,W_1>::maxval+1> tmpb(b);
	return (tmpa.val == tmpb.val);
}

template <int W_,  int W_1> bool operator <(const @(IClass)<W_>& a, const @(Class)<W_1>& b) {
	@(Class)<Template_Max<W_,W_1>::maxval+1> tmpa(a);
	@(Class)<Template_Max<W_,W_1>::maxval+1> tmpb(b);
	return (tmpa.val < tmpb.val);
}
template <int W_,  int W_1> bool operator !=(const @(IClass)<W_>& a, const @(Class)<W_1>& b) {
	return !(a == b);
}
template <int W_,  int W_1> bool operator >(const @(IClass)<W_>& a, const @(Class)<W_1>& b) {
	return (b < a);
}
template <int W_,  int W_1> bool operator <=(const @(IClass)<W_>& a, const @(Class)<W_1>& b) {
	return !(b<a);
}
template <int W_,  int W_1> bool operator >=(const @(IClass)<W_>& a, const @(Class)<W_1>& b) {
	return !(a<b);
}



// --------------------- BOOLEAN Comparisions "==,<=, <. >=, > , !=" -------------------------------------------
// Compare with doubles
template <int W_>	bool operator ==(const double& a, const @(Class)<W_> &b)  {return (b.to_double() == a);	}
template <int W_>	bool operator !=(const double& a, const @(Class)<W_> &b)  {return (b.to_double() != a);	}
template <int W_>	bool operator  <(const double& a, const @(Class)<W_> &b)  {return (b.to_double() > a);	}
template <int W_>	bool operator <=(const double& a, const @(Class)<W_> &b)  {return (b.to_double() >= a);	}
template <int W_>	bool operator  >(const double& a, const @(Class)<W_> &b)  {return (b.to_double() < a);	}
template <int W_>	bool operator >=(const double& a, const @(Class)<W_> &b)  {return (b.to_double() <= a);	}

template <int W_>	bool operator ==(const @(Class)<W_> &b, const double& a)  {return (b.to_double() == a);	}
template <int W_>	bool operator !=(const @(Class)<W_> &b, const double& a)  {return (b.to_double() != a);	}
template <int W_>	bool operator  <(const @(Class)<W_> &b, const double& a)  {return (b.to_double() < a);	}
template <int W_>	bool operator <=(const @(Class)<W_> &b, const double& a)  {return (b.to_double() <= a);	}
template <int W_>	bool operator  >(const @(Class)<W_> &b, const double& a)  {return (b.to_double() > a);	}
template <int W_>	bool operator >=(const @(Class)<W_> &b, const double& a)  {return (b.to_double() >= a);	}

// compare with uint64
template <int W_>	bool operator ==(const uint64_t& a, const @(Class)<W_> &b)  {return (b.to_int() == a);	}
template <int W_>	bool operator !=(const uint64_t& a, const @(Class)<W_> &b)  {return (b.to_int() != a);	}
template <int W_>	bool operator  <(const uint64_t& a, const @(Class)<W_> &b)  {return (b.to_int() > a);	}
template <int W_>	bool operator <=(const uint64_t& a, const @(Class)<W_> &b)  {return (b.to_int() >= a);	}
template <int W_>	bool operator  >(const uint64_t& a, const @(Class)<W_> &b)  {return (b.to_int() < a);	}
template <int W_>	bool operator >=(const uint64_t& a, const @(Class)<W_> &b)  {return (b.to_int() <= a);	}
template <int W_>	bool operator ==(const @(Class)<W_> &b, const uint64_t& a)  {return (b.to_int() == a);	}
template <int W_>	bool operator !=(const @(Class)<W_> &b, const uint64_t& a)  {return (b.to_int() != a);	}
template <int W_>	bool operator  <(const @(Class)<W_> &b, const uint64_t& a)  {return (b.to_int() < a);	}
template <int W_>	bool operator <=(const @(Class)<W_> &b, const uint64_t& a)  {return (b.to_int() <= a);	}
template <int W_>	bool operator  >(const @(Class)<W_> &b, const uint64_t& a)  {return (b.to_int() > a);	}
template <int W_>	bool operator >=(const @(Class)<W_> &b, const uint64_t& a)  {return (b.to_int() >= a);	}

// compare with int64
template <int W_>	bool operator ==(const int& a, const @(Class)<W_> &b)  {return (b.to_int() == a);	}
template <int W_>	bool operator !=(const int& a, const @(Class)<W_> &b)  {return (b.to_int() != a);	}
template <int W_>	bool operator  <(const int& a, const @(Class)<W_> &b)  {return (b.to_int() > a);	}
template <int W_>	bool operator <=(const int& a, const @(Class)<W_> &b)  {return (b.to_int() >= a);	}
template <int W_>	bool operator  >(const int& a, const @(Class)<W_> &b)  {return (b.to_int() < a);	}
template <int W_>	bool operator >=(const int& a, const @(Class)<W_> &b)  {return (b.to_int() <= a);	}

template <int W_>	bool operator ==(const @(Class)<W_> &b, const int& a)  {return (b.to_int() == a);	}
template <int W_>	bool operator !=(const @(Class)<W_> &b, const int& a)  {return (b.to_int() != a);	}
template <int W_>	bool operator  <(const @(Class)<W_> &b, const int& a)  {return (b.to_int() < a);	}
template <int W_>	bool operator <=(const @(Class)<W_> &b, const int& a)  {return (b.to_int() <= a);	}
template <int W_>	bool operator  >(const @(Class)<W_> &b, const int& a)  {return (b.to_int() > a);	}
template <int W_>	bool operator >=(const @(Class)<W_> &b, const int& a)  {return (b.to_int() >= a);	}

// Math Ops
 template <int W_> double operator +(const double& a, const @(Class)<W_>& b) {	 return(((double)a+(double)b));}
 template <int W_> double operator +(const @(Class)<W_>& b, const double& a) {		return(((double)a+(double)b));}
 template <int W_> double operator -(const double& a, const @(Class)<W_>& b) {		return(((double)a-(double)b));}
 template <int W_> double operator -(const @(Class)<W_>& a, const double& b) {		return(((double)a-(double)b));}
 template <int W_> double operator *(const double& a, const @(Class)<W_>& b) {		return(((double)a*(double)b));}
 template <int W_> double operator *(const @(Class)<W_>& a, const double& b) {		return(((double)a*(double)b));}
 template <int W_> double operator /(const double& a, const @(Class)<W_>& b) {		return(((double)a/(double)b));}
 template <int W_> double operator /(const @(Class)<W_>& a, const double& b) {		return(((double)a/(double)b));}
 template <int W_> double operator +(const int& a, const @(Class)<W_>& b) {		return(((double)a+(double)b));}
 template <int W_> double operator +(const @(Class)<W_>& b, const int& a) {		return(((double)a+(double)b));}
 template <int W_> double operator -(const int& a, const @(Class)<W_>& b) {		return(((double)a-(double)b));}
 template <int W_> double operator -(const @(Class)<W_>& a, const int& b) {		return(((double)a-(double)b));}
 template <int W_> double operator *(const int& a, const @(Class)<W_>& b) {		return(((double)a*(double)b));}
 template <int W_> double operator *(const @(Class)<W_>& a, const int& b) {		return(((double)a*(double)b));}
 template <int W_> double operator /(const int& a, const @(Class)<W_>& b) {		return(((double)a/(double)b));}
 template <int W_> double operator /(const @(Class)<W_>& a, const int& b) {		return(((double)a/(double)b));}
 template <int W_> double operator +(const uint64_t& a, const @(Class)<W_>& b) {		return(((double)a+(double)b));}
 template <int W_> double operator +(const @(Class)<W_>& b, const uint64_t& a) {	return(((double)a+(double)b));}
 template <int W_> double operator -(const uint64_t& a, const @(Class)<W_>& b) {		return(((double)a-(double)b));}
 template <int W_> double operator -(const @(Class)<W_>& a, const uint64_t& b) {		return(((double)a-(double)b));}
 template <int W_> double operator *(const uint64_t& a, const @(Class)<W_>& b) {		return(((double)a*(double)b));}
 template <int W_> double operator *(const @(Class)<W_>& a, const uint64_t& b) {		return(((double)a*(double)b));}
 template <int W_> double operator /(const uint64_t& a, const @(Class)<W_>& b) {		return(((double)a/(double)b));}
 template <int W_> double operator /(const @(Class)<W_>& a, const uint64_t& b) {		return(((double)a/(double)b));}

// Bool Ops
 template <int W_> @(Class)<W_+1> operator +(const bool& a, const @(Class)<W_>& b) {  return(sc_int<1>(a)+b);}
 template <int W_> @(Class)<W_+1> operator +(const @(Class)<W_>& a, const bool& b) {  return(a+sc_int<1>(b));}
 template <int W_> @(Class)<W_+1> operator -(const bool& a, const @(Class)<W_>& b) {  return(sc_int<1>(a)-b);}
 template <int W_> @(Class)<W_+1> operator -(const @(Class)<W_>& a, const bool& b) {  return(a-sc_int<1>(b));}


} // end of namespace @(Namespace)


#endif
    

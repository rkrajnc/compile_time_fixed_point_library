// DO NOT EDIT THIS FILE IT WAS AUTOMATICALLY GENERATED ON 2013/07/10
////////////////////////////////////////////////////////////////////////////// 
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

#ifndef SYSTEMC_SC_FT_SC_INT_20130710_CLASS_FUNCTIONS_H_
#define SYSTEMC_SC_FT_SC_INT_20130710_CLASS_FUNCTIONS_H_

#include <sc_common.h>
namespace sc_ft {


// IO functions
template <int NINT> std::ostream& operator <<(std::ostream& os, const sc_int<NINT>& r) {
  return os << r.to_int(); 
};
template <int NINT> std::istream& operator >>(std::istream& os, const sc_int<NINT>& r) {
  return os >> r;
};


// TEMPLATE functions for +,-,*,/ (divide returns double)

// addition
template <int W_,  int W_1>  sc_int<Template_Max<W_,W_1>::maxval+1>
	operator +(const sc_int<W_>& a, const sc_int<W_1>& b) {
	sc_int<Template_Max<W_,W_1>::maxval+1> tmp(a);
	tmp += b;
	return(tmp);
}

template <int W_,  int W_1>  sc_int<Template_Max<W_,W_1>::maxval+1>
	operator -(const sc_int<W_>& a, const sc_int<W_1>& b) {
	sc_int<Template_Max<W_,W_1>::maxval+1> tmp(a);
	tmp -= b;
	return(tmp);
}

	
// multiplication
template <int W_,  int W_1>  sc_int<W_+W_1>
	operator *(const sc_int<W_>& a, const sc_int<W_1>& b) {
	sc_int<W_+W_1> tmp(a);
	tmp *= b;
	return(tmp);
}
// division
template <int W_,  int W_1>  sc_int<W_>
	operator /(const sc_int<W_>& a, const sc_int<W_1>& b) {
	sc_int<W_> tmp(a);
	tmp /= b;
	return(tmp);
}
// <<
template <int W_,  int W_1>  sc_int<W_+W_1>
	operator <<(const sc_int<W_>& a, const sc_int<W_1>& shift) {
	sc_int<W_+W_1> tmp(a);
	tmp <<= shift;
	return(tmp);
}
// >>
template <int W_,  int W_1>  sc_int<W_>
	operator >>(const sc_int<W_>& a, const sc_int<W_1>& shift) {
	sc_int<W_> tmp(a);
	tmp >>= shift;
	return(tmp);
}

// Operations to support mixing with ints & doubles, etc

// Comparison operators "==,!=,<<=,>,>=" between this type and 'double'

// or
template <int W_, int W_1> sc_int<Template_Max<W_,W_1>::maxval>
	operator |(const sc_int<W_>& a, const sc_int<W_1>& b) {
	 sc_int<Template_Max<W_,W_1>::maxval> tmpa(a);
	 sc_int<Template_Max<W_,W_1>::maxval> tmpb(b);
	 tmpa.val |= tmpb.val;
	 return(tmpa);
}
template <int W_, int W_1> sc_int<Template_Max<W_,W_1>::maxval>
	operator &(const sc_int<W_>& a, const sc_int<W_1>& b) {
	 sc_int<Template_Max<W_,W_1>::maxval> tmpa(a);
	 sc_int<Template_Max<W_,W_1>::maxval> tmpb(b);
	 tmpa.val &= tmpb.val;
	 return(tmpa);
}
template <int W_, int W_1> sc_int<Template_Max<W_,W_1>::maxval>
	operator ^(const sc_int<W_>& a, const sc_int<W_1>& b) {
	 sc_int<Template_Max<W_,W_1>::maxval> tmpa(a);
	 sc_int<Template_Max<W_,W_1>::maxval> tmpb(b);
	 tmpa.val ^= tmpb.val;
	 return(tmpa);
}

template <int W_,  int W_1> bool operator ==(const sc_int<W_>& a, const sc_int<W_1>& b) {
	sc_int<Template_Max<W_,W_1>::maxval> tmpa(a);
	sc_int<Template_Max<W_,W_1>::maxval> tmpb(b);
	return (tmpa.val == tmpb.val);
}

template <int W_,  int W_1> bool operator <(const sc_int<W_>& a, const sc_int<W_1>& b) {
	sc_int<Template_Max<W_,W_1>::maxval> tmpa(a);
	sc_int<Template_Max<W_,W_1>::maxval> tmpb(b);
	return (tmpa.val < tmpb.val);
}
template <int W_,  int W_1> bool operator !=(const sc_int<W_>& a, const sc_int<W_1>& b) {
	return !(a == b);
}

template <int W_,  int W_1> bool operator >(const sc_int<W_>& a, const sc_int<W_1>& b) {
	return (b < a);
}
template <int W_,  int W_1> bool operator <=(const sc_int<W_>& a, const sc_int<W_1>& b) {
	return !(b<a);
}
template <int W_,  int W_1> bool operator >=(const sc_int<W_>& a, const sc_int<W_1>& b) {
	return !(a<b);
}

} // end of namespace sc_ft


#endif
    


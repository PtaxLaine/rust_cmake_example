#![allow(private_no_mangle_fns)]

#[no_mangle]
#[cfg(feature = "lib_feature")]
pub extern "C" fn foobar(){
	println!("lib.rs:{}", line!());
}

#[no_mangle]
#[cfg(feature = "bin_feature")]
pub extern "C" fn foobar(){
	println!("lib.rs:{}", line!());
}

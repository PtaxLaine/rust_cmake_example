mod lib;

fn main(){
	println!("bin.rs:{}", line!());
	lib::foobar();
	println!("bin.rs:{}", line!());
}
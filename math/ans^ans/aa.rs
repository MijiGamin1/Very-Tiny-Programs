use std::io;
fn main() {
	let mut x = String::new();
	let mut it = 1;
	println!("type in number between zero and one");
	match io::stdin().read_line(&mut x) {
		Ok(_) => {
			let mut int = x.trim().parse::<f64>().unwrap();
			while !int.is_infinite() & (int != 1.0){
				int = int.powf(int);
				println!("{}", int);
				it += 1;
			}
			let fin = "It took you ".to_owned() + &it.to_string() + " ans^ans'es to reach " + &int.to_string() + "!";
			println!("{}", fin);
		},
		Err(_) => {
			println!("how");
		}
	}
}
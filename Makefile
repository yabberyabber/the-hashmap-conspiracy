default: cpp/Main java_hashmap/Main.class go/main rust/target/debug/rust
	python driver.py

clean:
	-rm -f cpp/Main
	-rm -f java_hashmap/Main.class
	-rm -f go/main
	-rm -rf rust/target

cpp/Main: cpp/main.cpp
	g++ cpp/main.cpp -std=c++11 -o cpp/Main

java_hashmap/Main.class: java_hashmap/main.java
	javac java_hashmap/main.java -s java_hashmap

go/main: go/main.go
	cd go; go build main.go

rust/target/debug/rust: rust/main.rs rust/Cargo.toml
	cd rust; cargo build --release

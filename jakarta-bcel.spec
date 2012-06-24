Summary:	Byte Code Engineering Library
Summary(pl.UTF-8):   Biblioteka do obróbki bajtkodu Javy
Name:		jakarta-bcel
Version:	5.1
Release:	2
License:	Apache Software License
Group:		Development/Languages/Java
# a lot of junk (all other formats) inside -src.tar.gz, use -src.zip
Source0:	http://www.apache.org/dist/jakarta/bcel/source/bcel-%{version}-src.zip
# Source0-md5:	23767d4e735543c25b950ab86c8f56b1
Patch0:		%{name}-build.patch
Patch1:		%{name}-manifest.patch
Patch2:		%{name}-jdk15.patch
URL:		http://jakarta.apache.org/bcel/
BuildRequires:	ant
BuildRequires:	jakarta-regexp
BuildRequires:	jpackage-utils
BuildRequires:	rpmbuild(macros) >= 1.300
BuildRequires:	unzip
Requires:	jakarta-regexp
Provides:	bcel
BuildArch:	noarch
ExclusiveArch:	i586 i686 pentium3 pentium4 athlon %{x8664} noarch
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
The Byte Code Engineering Library (formerly known as JavaClass) is
intended to give users a convenient possibility to analyze, create,
and manipulate (binary) Java class files (those ending with .class).
Classes are represented by objects which contain all the symbolic
information of the given class: methods, fields and byte code
instructions, in particular. Such objects can be read from an existing
file, be transformed by a program (e.g. a class loader at run-time)
and dumped to a file again. An even more interesting application is
the creation of classes from scratch at run-time. The Byte Code
Engineering Library (BCEL) may be also useful if you want to learn
about the Java Virtual Machine (JVM) and the format of Java .class
files. BCEL is already being used successfully in several projects
such as compilers, optimizers, obsfuscators and analysis tools, the
most popular probably being the Xalan XSLT processor at Apache.

%description -l pl.UTF-8
BCEL (Byte Code Engineering Library, poprzednio znana jako JavaClass)
ma umożliwić wygodne analizowanie, tworzenie i obróbkę (binarnych)
plików klas Javy (tych z nazwą kończącą się na .class). Klasy są
reprezentowane przez obiekty zawierające wszystkie symboliczne
informacje o danej klasie, w szczególności metody, pola i instrukcje
bajtkodu. Obiekty te mogą być odczytywane z istniejącego pliku,
przekształcane przez program (np. wczytujący klasy w czasie działania)
i zrzucane z powrotem do pliku. Jeszcze ciekawszym zastosowaniem jest
tworzenie klas od zera w czasie działania programu. Biblioteka BCEL
może być także użyteczna, jeśli chcemy nauczyć się czegoś o maszynie
wirtualnej Javy (JVM) oraz formacie plików .class. BCEL jest używana z
sukcesem w różnych projektach, takich jak kompilatory, optymalizatory,
narzędzia utrudniające analizę oraz narzędzia do analizy, z których
najpopularniejszym jest procesor XSLT Xalan.

%package javadoc
Summary:	Byte Code Engineering Library documentation
Summary(pl.UTF-8):   Dokumentacja do biblioteki do obróbki bajtkodu Javy
Group:		Documentation
Requires:	jpackage-utils
Obsoletes:	jakarta-bcel-doc

%description javadoc
Byte Code Engineering Library documentation.

%description javadoc -l pl.UTF-8
Dokumentacja do biblioteki do obróbki bajtkodu Javy.

%prep
%setup -q -n bcel-%{version}
%patch0 -p1
%patch1 -p1
%patch2 -p1
find . -name "*.jar" -exec rm -f {} \;

%build

export CLASSPATH="`build-classpath regexp`"
export JAVA_HOME="%{java_home}"

%ant jar apidocs

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT{%{_javadir},%{_javadocdir}/%{name}-%{version}}

cp -p bin/bcel.jar $RPM_BUILD_ROOT%{_javadir}/bcel-%{version}.jar
ln -sf bcel-%{version}.jar $RPM_BUILD_ROOT%{_javadir}/bcel.jar

cp -R docs/api/* $RPM_BUILD_ROOT%{_javadocdir}/%{name}-%{version}

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc LICENSE.txt
%{_javadir}/*.jar

%files javadoc
%defattr(644,root,root,755)
%doc %{_javadocdir}/%{name}-%{version}

---
title: A descent principle for base change
decls:
  - UpperTheory.Et.E3.n9
  - UpperTheory.Et.E3.n24
  - UpperTheory.Et.E3.n34
status: drafted
drafted_by: writer@claude-opus-5-5
---
## A descent principle for base change

In this section we prove a principle that reduces a base change statement for a ring map to a statement at points. Let $\varphi : A \to Y$ be a ring map. We want to show that for every $A$-algebra $C$ in a class $P$, the map $C \to Y \otimes_A C$ is an equivalence for $\mathbb{Z}/q(i)$. The principle says that it is enough to cover each $C$ by an integral map with surjective spectrum, and to check the statement after an ind-étale map at each point of the cover. Section 14 applies it twice in the proof of axiom E3. The proof is an induction on the degree. In each degree it uses Čech descent along étale covers and along integral covers, and the relative cohomology of a map.

### Base change properties

Throughout, $q \geq 1$ and $i$ are fixed, $A$ is a ring in which $q$ is a unit, and $\varphi : A \to Y$ is a ring map. We write $H^n(B)$ for $H^n(\mathrm{sp}(B), \mathbb{Z}/q(i))$ and $f^*$ for the map on cohomology induced by a ring map $f$. We assume the axioms A1 to A5, A9, B1, B2, B4, C3 and C4 of section 1. Other chapters of this volume prove them.

**Definition 3.13.1 (Equivalence of rings).** A ring map $f : B \to B'$ is an *equivalence* if $\operatorname{Spec} f$ is an equivalence for $\mathbb{Z}/q(i)$, that is, if $f^* : H^n(B) \to H^n(B')$ is bijective for all $n$. For $n \in \mathbb{Z}$, we say that $f$ is *good in degree $n$* if $f^*$ is surjective on $H^{n-1}$ and injective on $H^n$.

A map is an equivalence if and only if it is good in every degree.

**Definition 3.13.2 (Base change property).** Let $c : A \to C$ be a ring map. We say that $\varphi$ has *base change along $c$* if for every pushout square
$$
\begin{array}{ccc}
A & \xrightarrow{\ \varphi\ } & Y \\
{\scriptstyle c} \downarrow & & \downarrow \\
C & \xrightarrow{\ \varphi'\ } & Y'
\end{array}
$$
the map $\varphi' : C \to Y' = Y \otimes_A C$ is an equivalence. We say that $\varphi$ has *base change along $c$ in degree $n$* if every such $\varphi'$ is good in degree $n$.

**Definition 3.13.3 (Closed classes).** A *class of $A$-algebras* is a property $P$ of ring maps $c : A \to C$. The class is *closed under pushouts* if for every $c : A \to C$ and maps $C \to D$, $C \to E$ with $c$, $A \to D$ and $A \to E$ in $P$, the map $A \to D \otimes_C E$ is in $P$. It is *closed under étale maps* if $c \in P$ and $C \to D$ étale imply that $A \to D$ is in $P$.

A ring map is *ind-étale* if it is a filtered colimit of étale maps. A ring map $g : C \to D$ is *surjective on spectra* if every prime of $C$ is the preimage of a prime of $D$.

**Definition 3.13.4 (Base change at points).** Let $d : A \to D$ be a ring map. We say that $\varphi$ has *base change at the points of $D$* if for every prime $\mathfrak{r}$ of $D$ there are an ind-étale map $o : D \to O$ and a prime $\mathfrak{Q}$ of $O$ over $\mathfrak{r}$ such that $\varphi$ has base change along $o \circ d$.

### Relative cohomology

For a map of spaces $f : U \to E$ the relative cohomology $H^n(f)$ is the cohomology of the mapping cone of the map of cochain complexes induced by $f$, with coefficients $\mathbb{Z}/q(i)$. A commutative square, with $f' : U' \to E'$, $u : U' \to U$, $e : E' \to E$ and $f \circ u = e \circ f'$, induces a map $H^n(f) \to H^n(f')$. We use the following properties.

1. *(Exact sequence.)* There is a natural long exact sequence
$$
\cdots \to H^{n-1}(E) \xrightarrow{f^*} H^{n-1}(U) \xrightarrow{\ \partial\ } H^n(f) \to H^n(E) \xrightarrow{f^*} H^n(U) \to \cdots,
$$
and the maps induced by a square commute with all maps of these sequences.
2. *(Equivalences.)* If in a square as above $u$ and $e$ are equivalences, then $H^n(f) \to H^n(f')$ is injective for every $n$.
3. *(Composition.)* The map induced by a composite of squares is the composite of the induced maps.

### Facts that we take as given

We take as given the following facts. In each of them $P$ is a class of $A$-algebras that is closed under pushouts and under étale maps, $n \in \mathbb{Z}$, and $\varphi$ has base change in every degree $m < n$ along every map in $P$. We call this the *lower degree hypothesis*.

1. *(Étale Čech nerves.)* If $e : D \to E$ is étale and surjective on spectra, then the augmentation of the Čech nerve of $\operatorname{Spec} e$ is an equivalence, and the same holds for every base change of $e$. This is axiom A2.
2. *(Levels of the Čech nerves.)* Let $d : A \to D$ be in $P$, let $\varphi' : D \to Y'$ be the pushout of $\varphi$, let $e : D \to E$ be étale and surjective on spectra with $e \circ d$ in $P$, and let $u : Y' \to Y'' = Y' \otimes_D E$ and $\varphi'' : E \to Y''$ be the pushout maps. Then there is a map $g$ from the Čech nerve of $\operatorname{Spec} u$ to the Čech nerve of $\operatorname{Spec} e$, over $\operatorname{Spec} \varphi'$ through the augmentations and compatible with the inclusions of level $0$, such that the square from $\operatorname{Spec} \varphi''$ to $g$ induces an injective map on relative cohomology in degree $n$. The proof filters the Čech nerves and works level by level with the lower degree hypothesis.
3. *(Killing cokernels.)* In the setting of fact 2, assume that $\varphi$ has base change at the points of $D$. For each $y \in H^{n-1}(Y')$ there is an étale map $e : D \to E$, surjective on spectra, with $e \circ d$ in $P$, such that $u^* y$ lies in the image of $\varphi''^*$. The proof finds such an $e$ near each point, through the ind-étale maps at points and B1, and takes the product of finitely many of them.
4. *(Kernels.)* Assume that for every $c \in P$ at whose points $\varphi$ has base change, every pushout $\varphi'$ of $\varphi$ along $c$ is surjective on $H^{n-1}$. If $d : A \to D$ is in $P$ and $\varphi$ has base change at the points of $D$, then every pushout of $\varphi$ along $d$ is injective on $H^n$. The proof uses the lemma on relative descent below and the fact that the cohomology of a finite disjoint union of affine schemes is the product of their cohomologies.
5. *(Integral descent.)* Let $c : A \to C$ be in $P$ and $g : C \to D$ integral and surjective on spectra, with $g \circ c$ in $P$. If $\varphi$ has base change along $g \circ c$ in degree $n$, then it has base change along $c$ in degree $n$. The proof uses B4 for the Čech nerve of $\operatorname{Spec} g$ and the lower degree hypothesis on its levels.

### Relative descent

**Lemma 3.13.5 (Relative descent).** Let $P$ and $n$ be as above, with the lower degree hypothesis. Let $d : A \to D$ be in $P$, and let $\varphi'$, $e$, $u$ and $\varphi''$ be as in fact 2. Then the map
$$
H^n(\operatorname{Spec} \varphi') \to H^n(\operatorname{Spec} \varphi'')
$$
induced by the square with sides $\operatorname{Spec} u$ and $\operatorname{Spec} e$ is injective.

Lean: `UpperTheory.Et.E3.n34`.

*Proof.* Let $\check{C}_e$ and $\check{C}_u$ be the Čech nerves of $\operatorname{Spec} e$ and $\operatorname{Spec} u$, and let $g : \check{C}_u \to \check{C}_e$ be the map of fact 2. The square of $\operatorname{Spec} \varphi''$ and $\operatorname{Spec} \varphi'$ factors as the composite of two squares: first from $\operatorname{Spec} \varphi''$ to $g$, through the inclusions of level $0$, and then from $g$ to $\operatorname{Spec} \varphi'$, through the augmentations. The map $u$ is a base change of $e$, so by fact 1 both augmentations are equivalences. By property 2 the second square gives an injective map on relative cohomology. By fact 2 the first square gives an injective map in degree $n$. By property 3 the map of the lemma is the composite of these two maps, so it is injective. $\square$

### Local descent

**Proposition 3.13.6 (Local descent).** Let $P$ be a class of $A$-algebras that is closed under pushouts and under étale maps, and let $n \in \mathbb{Z}$. Assume the lower degree hypothesis for $n$. Let $d : A \to D$ be in $P$, and assume that $\varphi$ has base change at the points of $D$. Then $\varphi$ has base change along $d$ in degree $n$.

Lean: `UpperTheory.Et.E3.n24`.

*Proof.* We first show a claim. In the setting of fact 2, let $y \in H^{n-1}(Y')$, and suppose that $u^* y = \varphi''^* z$ for some $z \in H^{n-1}(E)$. Then $y$ lies in the image of $\varphi'^*$. Indeed, let $\partial$ and $\partial''$ be the boundary maps of property 1 for $\operatorname{Spec} \varphi'$ and $\operatorname{Spec} \varphi''$. By naturality the image of $\partial y$ in $H^n(\operatorname{Spec} \varphi'')$ is $\partial''(u^* y) = \partial''(\varphi''^* z)$, and this is $0$ by exactness. By the lemma on relative descent $\partial y = 0$, and by exactness $y$ is in the image of $\varphi'^*$.

Now let $c : A \to C$ be in $P$ such that $\varphi$ has base change at the points of $C$, and let $\varphi' : C \to Y'$ be a pushout of $\varphi$. Let $y \in H^{n-1}(Y')$. Fact 3 gives an étale map $e$, surjective on spectra, with $e \circ c$ in $P$ and $u^* y$ in the image of $\varphi''^*$. By the claim, $y$ is in the image of $\varphi'^*$. So $\varphi'^*$ is surjective on $H^{n-1}$.

This is the hypothesis of fact 4. Fact 4, applied to $d$, says that every pushout of $\varphi$ along $d$ is injective on $H^n$. With surjectivity on $H^{n-1}$ for $c = d$, every such pushout is good in degree $n$. $\square$

### The descent principle

**Proposition 3.13.7 (Descent principle).** Let $P$ be a class of $A$-algebras that is closed under pushouts and under étale maps. Suppose that for every $c : A \to C$ in $P$ there is an integral map $g : C \to D$, surjective on spectra, with $g \circ c$ in $P$, such that $\varphi$ has base change at the points of $D$, where $D$ is an $A$-algebra through $g \circ c$. Then $\varphi$ has base change along every $c$ in $P$.

Lean: `UpperTheory.Et.E3.n9`.

*Proof.* For $k \geq 0$ let $S(k)$ be the statement: for every $m < k$ and every $c$ in $P$, $\varphi$ has base change along $c$ in degree $m$. We prove $S(k)$ by induction on $k$.

The statement $S(0)$ concerns degrees $m < 0$. By A9 the groups $H^{m-1}$ and $H^m$ vanish for $m < 0$, so every map is good in degree $m$.

Suppose that $S(k)$ holds. It remains to treat the degree $m = k$. Let $c : A \to C$ be in $P$, and let $g : C \to D$ be as in the hypothesis. The statement $S(k)$ is the lower degree hypothesis for $n = k$. By the proposition on local descent, applied to $g \circ c$, the map $\varphi$ has base change along $g \circ c$ in degree $k$. By fact 5 it has base change along $c$ in degree $k$. This proves $S(k + 1)$.

Now let $c$ be in $P$ and $\varphi'$ a pushout of $\varphi$ along $c$. For each $n \in \mathbb{Z}$, $S(k)$ with $k > n$ shows that $\varphi'$ is good in degree $n$. So $\varphi'^*$ is injective on every $H^n$ and surjective on every $H^{n-1}$, and $\varphi'$ is an equivalence. $\square$

The hypothesis asks for base change at points only after the integral cover $g$. This is the form in which section 14 uses it: the cover makes the rings absolutely integrally closed, and at points the statement becomes one about strictly henselian rings.

**Remark 3.13.8 (Formalization).** The names `n1` to `n84` number the steps of the chain that proves E3 ([N81.lean](lean:Development/AutomorphicArithmetic/CommutativeAlgebra/EtaleCohomology/N81.lean#L153)) and carry no meaning; `N81.lean` itself is named after the step `n81`. The axioms of this section come as one hypothesis, the conjunction of the eleven axioms, and each statement assumes $q \neq 0$. Rings are objects of the category of commutative rings, and pushouts are pushout squares in this category, so "every pushout square" in the definitions means every square with the universal property, not only the tensor product. Relative cohomology is defined as the cohomology of the mapping cone of the map of chain complexes. The development states and proves exactness at $H^n(E)$ and the injectivity of $H^n(f) \to H^n(E)$ when $f^*$ is surjective on $H^{n-1}$ ([TruncKerPf.lean](lean:Development/EtaleCohomology/EtaleSheaves/TruncKerPf.lean#L9)); the claim in the proof of local descent is a separate step whose proof we have not unfolded, and we give the standard argument with the boundary map. The proof of the lemma on relative descent follows [RelDescPf.lean](lean:Development/EtaleCohomology/EtaleSheaves/RelDescPf.lean#L51). We have not unfolded the proofs of facts 2 to 5; the sketches above follow the names and statements of their steps.

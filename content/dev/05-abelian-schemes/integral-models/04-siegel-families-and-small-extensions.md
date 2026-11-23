---
title: Siegel families and small extensions
decls:
  - GlobalTheory.SmallClassify.classified_of_small
  - GlobalTheory.T.exists_siegPB_lift_of_quotient_lift
status: drafted
drafted_by: writer@claude-opus-5-5
---
## Siegel families and small extensions

The proof of representability starts from a Siegel family. This is a smooth quasi-projective scheme over $B_M$ with a principal Siegel object that classifies principal Siegel objects over reduced schemes of characteristic $0$ in a dense set, and that does so with unique maps over local rings. Such a family comes from geometric invariant theory (Mumford, Fogarty and Kirwan, *Geometric Invariant Theory*, Chapter 7) or from complex uniformization, and we take its existence as given in a later section. Here and in the next sections we show that a Siegel family classifies every principal Siegel object over every scheme. This section does the main step. Let $C$ be a local Artinian ring and $e \in C$ an element killed by the maximal ideal. If the family classifies the restrictions to $C/(e)$, it classifies objects over $C$. The proof is the argument of Schlessinger ("Functors of Artin rings", Trans. Amer. Math. Soc. 130 (1968), 208 to 222, §2) for the pinch $C \times_{C/(e)} C$, combined with the smoothness of the family and the gluing of the previous section.

### Siegel families

We keep the notation of the first section: $h \geq 1$, $M \geq 3$ is odd, $B_M = \mathbb{Z}[\zeta_M, 1/M]$, and Siegel objects have genus $h$ and level $M$. Maps of Siegel objects and principal Siegel objects are defined in the previous section.

**Definition 8.4.1 (Siegel family).** A *Siegel family* of genus $h$ and level $M$ consists of a scheme $X$, a map $s : X \to \operatorname{Spec} B_M$ that is quasi-projective and smooth of relative dimension $h(h+1)/2$, and a principal Siegel object $u$ over $s$, with the following two properties.

1. Let $S$ be a reduced scheme with a map $s' : S \to \operatorname{Spec} B_M$ such that the points of $S$ over the generic point of $\operatorname{Spec} B_M$ are dense. Then for every principal Siegel object $c$ over $s'$ there is $f : S \to X$ with $s f = s'$ and a map $c \to u$ over $f$.
2. Let $R$ be a local ring, $c$ a Siegel object over $\operatorname{Spec} R$, and $x, y : \operatorname{Spec} R \to X$ with $s x = s y$, such that there are maps $c \to u$ over $x$ and over $y$. Then $x = y$.

Let $F = (X, s, u)$ be a Siegel family and $c$ a Siegel object over $s' : S \to \operatorname{Spec} B_M$. We say that $F$ *classifies* $c$ if there are $f : S \to X$ with $s f = s'$ and a map $c \to u$ over $f$.

We use the following results on maps of Siegel objects. We state them as we use them.

1. (Pullbacks.) Let $c$ be a Siegel object over $s : S \to \operatorname{Spec} B_M$ and $f : S' \to S$. Then there is a Siegel object $c'$ over $s f$ with a map $c' \to c$ over $f$. If $c$ is principal, so is $c'$.
2. (Identity, composition and cancellation.) There is a map $c \to c$ over the identity. If $c' \to c$ over $f$ and $c'' \to c'$ over $f'$, then $c'' \to c$ over $f f'$. If $c' \to c$ over $f$ and $c'' \to c$ over $f f'$, then $c'' \to c'$ over $f'$.
3. (Dual numbers.) Let $F$ be a Siegel family, $k$ a field, and $k[\varepsilon]$ the dual numbers. Then $F$ classifies every principal Siegel object over every map $\operatorname{Spec} k[\varepsilon] \to \operatorname{Spec} B_M$.
4. (Maps from a fibre product.) Let $P = B_1 \times_{B_0} B_2$ be a cartesian square of rings with $P$ local and Artinian, $B_0 \neq 0$, and the projections $P \to B_1$ and $P \to B_2$ surjective. Then two maps $\operatorname{Spec} B_1 \to Z$ and $\operatorname{Spec} B_2 \to Z$ to a scheme $Z$ that agree on $\operatorname{Spec} B_0$ come from a unique map $\operatorname{Spec} P \to Z$.
5. (Determination over a fibre product.) Let $P = R_1 \times_{R_0} R_2$ be an Artinian fibre product and $c$, $c'$ principal Siegel objects over $P$. If there are a Siegel object $c_1$ over $R_1$ with maps $c_1 \to c$ and $c_1 \to c'$ over $f_1$, and a Siegel object $c_2$ over $R_2$ with maps $c_2 \to c$ and $c_2 \to c'$ over $f_2$, then there is a map $c' \to c$ over the identity.
6. (Local lifting.) Let $s : X \to \operatorname{Spec} R$ be smooth, $C$ an $R$-algebra and $I \subseteq C$ an ideal with $I^2 = 0$. Every $R$-map $\operatorname{Spec}(C/I) \to X$ lifts, on some open neighbourhood of each point, to an $R$-map from an open subscheme of $\operatorname{Spec} C$ (EGA IV$_4$, §17).

Result 3 is a statement about the tangent space of the moduli problem. Result 5 is the injectivity part of Schlessinger's condition (H1).

### Two lemmas

**Lemma 8.4.2 (Lifting along a square zero extension).** Let $s : X \to \operatorname{Spec} R$ be smooth, let $C$ be a local $R$-algebra and $e \in C$ with $e^2 = 0$. Then every $R$-map $x_0 : \operatorname{Spec}(C/(e)) \to X$ is the restriction of an $R$-map $x_1 : \operatorname{Spec} C \to X$.

Lean: `GlobalTheory.SmallClassify.lift_lemma`.

*Proof.* The ideal $(e)$ has square zero. Result 6 gives an open $W$ of $\operatorname{Spec} C$ that contains the closed point and a lift $W \to X$ of $x_0$ restricted to $W$. Every open set of the spectrum of a local ring that contains the closed point is the whole space. So $W = \operatorname{Spec} C$. $\square$

**Lemma 8.4.3 (The pinch).** Let $C$ be a local Artinian ring with residue field $k$ and maximal ideal $\mathfrak{m}$, and let $e \in \mathfrak{m}$ be nonzero with $\mathfrak{m} e = 0$. Then there are a local Artinian ring $P$ and ring maps $i : C \to P$, $p, \sigma : P \to C$ and $q : P \to k[\varepsilon]$ with $p i = \sigma i = 1$, such that $p$ and $q$ are surjective and the two squares
$$
\begin{aligned}
P &= C \times_{C/(e)} C \quad \text{(along } p, \sigma\text{)}, \\
P &= C \times_k k[\varepsilon] \quad \text{(along } p, q\text{)}
\end{aligned}
$$
are cartesian. In the second square $C \to k$ is the residue map and $k[\varepsilon] \to k$ sends $\varepsilon$ to $0$.

Lean: `GlobalTheory.SmallClassify.ring_lemma`.

*Proof.* Since $\mathfrak{m} e = 0$, the map $C \to C$, $c \mapsto ce$, factors through an additive map $\varphi : k \to C$ with $\varphi(\bar{c}) = ce$. It is injective: if $ce = 0$ and $c$ is a unit, then $e = 0$. Its image is the ideal $(e)$. Let $P = \{(a, y_0 + y_1 \varepsilon) \in C \times k[\varepsilon] : \bar{a} = y_0\}$, let $p$ and $q$ be the two projections, let $i(c) = (c, \bar{c})$, and let $\sigma(a, y_0 + y_1 \varepsilon) = a + \varphi(y_1)$. A short computation with $\varphi(y)\varphi(y') = 0$ and $a \varphi(y) = \varphi(\bar{a} y)$ shows that $\sigma$ is a ring map. Then $p i = \sigma i = 1$, the second square is cartesian by construction, and $p$, $q$ are surjective. The map $(p, \sigma) : P \to C \times_{C/(e)} C$ is bijective: given $(a, b)$ with $b - a \in (e)$, there is a unique $y_1 \in k$ with $\varphi(y_1) = b - a$. So the first square is cartesian. The ring $P$ is a subring of $C \times k[\varepsilon]$ that is finite over $C$ through $i$, so it is Artinian. Its elements $(a, y)$ with $a$ a unit are units, so $P$ is local. $\square$

### The small extension theorem

**Theorem 8.4.4 (Classification over a small extension).** Let $h \geq 1$, let $M \geq 3$ be odd, and let $F = (X, s, u)$ be a Siegel family of genus $h$ and level $M$. Let $C$ be a local Artinian ring with maximal ideal $\mathfrak{m}$, and let $e \in \mathfrak{m}$ with $\mathfrak{m} e = 0$. Let $\beta : B_M \to C$ and let $c$ be a principal Siegel object over $\operatorname{Spec} C$. Suppose that $F$ classifies every Siegel object $c_0$ over $\operatorname{Spec}(C/(e))$ with a map $c_0 \to c$ over the quotient map. Then $F$ classifies $c$.

Lean: `GlobalTheory.SmallClassify.classified_of_small` (also `GlobalTheory.T.exists_siegPB_lift_of_quotient_lift`).

*Proof.* Let $\pi : C \to C/(e)$ be the quotient map. By result 1 there is a pullback $c_0$ of $c$ along $\pi$, and by hypothesis there are $x_0 : \operatorname{Spec}(C/(e)) \to X$ over $B_M$ and a map $c_0 \to u$ over $x_0$. If $e = 0$, then $\pi$ is an isomorphism and $x_0 \pi^{-1}$ classifies $c$ by result 2. Suppose that $e \neq 0$.

Since $e^2 = 0$, the first lemma gives $x_1 : \operatorname{Spec} C \to X$ over $B_M$ that restricts to $x_0$. Let $P$, $i$, $p$, $\sigma$, $q$ be as in the second lemma, and give $P$ the map $i \beta$ from $B_M$. Let $c_1$ be a pullback of $u$ along $x_1$, seen over $C$ through $p$, and let $c_2 = c$, seen over $C$ through $\sigma$. Both are principal. A pullback $c_0'$ of $u$ along $x_0$ is a pullback of $c_1$ along $\pi$, since $x_1$ restricts to $x_0$. It is also a pullback of $c$ along $\pi$, since $c_0 \to u$ over $x_0$. These two facts use result 2. The [gluing theorem for principal Siegel objects](/entry/exists-principal-glue/), applied to $P = C \times_{C/(e)} C$, gives a principal Siegel object $e'$ over $P$ with maps $c_1 \to e'$ over $p$ and $c \to e'$ over $\sigma$.

Let $e_\varepsilon$ be a pullback of $e'$ along $q$, a principal Siegel object over $k[\varepsilon]$. Result 3 gives $v : \operatorname{Spec} k[\varepsilon] \to X$ that classifies $e_\varepsilon$. Let $\rho : C \to k$ and $\varepsilon_0 : k[\varepsilon] \to k$ be the maps of the second square, and let $c_k$ be a pullback of $c_1$ along $\rho$. Then $c_k$ is a pullback of $u$ along $x_1 \rho$. Since $\rho p = \varepsilon_0 q$ and $e'$ restricts to $c_1$ along $p$ and to $e_\varepsilon$ along $q$, the object $c_k$ is also a pullback of $e_\varepsilon$ along $\varepsilon_0$, and so a pullback of $u$ along $v \varepsilon_0$. Property 2 of a Siegel family, for the local ring $k$, shows that $x_1 \rho = v \varepsilon_0$ as maps $\operatorname{Spec} k \to X$.

Result 4, applied to $P = C \times_k k[\varepsilon]$ with $p$ and $q$ surjective and $k \neq 0$, gives $w : \operatorname{Spec} P \to X$ with $w p = x_1$ and $w q = v$. The uniqueness in result 4, applied to $Z = \operatorname{Spec} B_M$, shows that $w$ is a map over $B_M$. Let $e''$ be a pullback of $u$ along $w$. Then $c_1$ is a pullback of $e''$ along $p$, and $e_\varepsilon$ is a pullback of $e''$ along $q$. Result 5, applied to $e'$ and $e''$ over $P = C \times_k k[\varepsilon]$, gives a map $e' \to e''$ over the identity. Now compose the maps $c \to e'$ over $\sigma$, $e' \to e''$ and $e'' \to u$ over $w$. They give a map $c \to u$ over $f = w \sigma$, and $f$ is a map over $B_M$ since $\sigma i = 1$. $\square$

The hypothesis of the theorem asks $F$ to classify every pullback $c_0$ of $c$, which is principal by result 1. The proof uses it for one $c_0$.

**Remark 8.4.5 (Formalization).** The statement asks for a lift of every Siegel object $c_0$ over $C/(e)$ with a map $c_0 \to c$; principality of $c_0$ is not required there, since it follows: [ClassifiedOfSmallStatement.lean](lean:Development/AbelianVarietyTheory/Proofs/DivisorProofs/ClassifiedOfSmallStatement.lean#L11). The case $e = 0$ is a separate branch with the inverse of the quotient map: [ClassifiedOfSmall.lean](lean:Development/AbelianVarietyTheory/Proofs/DivisorProofs/ClassifiedOfSmall.lean#L216). The pinch ring is built as a subring of $C \times k[\varepsilon]$: [ClassifiedOfSmall.lean](lean:Development/AbelianVarietyTheory/Proofs/DivisorProofs/ClassifiedOfSmall.lean#L74). Result 4 assumes that the projections $P \to B_1$ and $P \to B_2$ are surjective, and not the maps to $B_0$. A Siegel family is a structure with fields for smoothness, quasi-projectivity, the universal object, and properties 1 and 2: [IsSeparatedOfIsQProjOver.lean](lean:Development/AbelianVarietyTheory/Definitions/ModuliSpaces/IsSeparatedOfIsQProjOver.lean#L18). The relative dimension $h(h+1)/2$ is a division of natural numbers, which is exact. The statement wrapper raises the heartbeat limit and calls the proof through a `first` tactic. We read the statements of results 1 to 6, not their proofs.

---
title: Ordinary vanishing and the Bloch-Kato Selmer group
decls:
  - GlobalTheory.T.dualSelmer_unbounded_order_nonzero_ordinaryClass
  - GlobalTheory.Ord2.gw_limit
  - GlobalTheory.T.ordinarySelmer_vanishes_of_dual_vanishes
  - GlobalTheory.Ord2.grZero_of_grZero_dual1
  - GlobalTheory.Ord2.es_vanish
  - GlobalTheory.Ord2.vanishOrdL_of_zetaUr
status: drafted
drafted_by: writer@claude-opus-5-5
---
## Ordinary vanishing and the Bloch-Kato Selmer group

This section ends the argument of Sections 20 to 23. It proves four statements. First, dual Selmer classes of unbounded order modulo $\ell^n$ give a nonzero ordinary Selmer class of $W^*$. Second, the ordinary Selmer group of $W$ vanishes when that of $W^*$ vanishes. Third, an Euler system class for $W$ in normal form makes the Bloch-Kato Selmer group of $W$ vanish. Fourth, the vanishing holds for every ordinary representation that comes from a newform, if such representations have zeta classes. The fourth statement is used by [the vanishing of two Bloch-Kato Selmer groups](/entry/two-s/), and its hypothesis is the statement of [the Euler system class with an unramified source](/entry/zeta-ur/).

We keep the notation of Sections 20 to 23. The ordinary Selmer group of $V$ vanishes, for $V = W$ or $V = W^*$, if every cocycle for $V$ that is unramified outside $\ell$ and ordinary at $A$ is a coboundary (Section 22).

### From unbounded order to a nonzero class

**Theorem 6.24.1 (A nonzero dual class).** Assume the cohomological inputs of Section 21. Let $W$ be in normal form for $(e, S, A)$, and let $\mathcal{O}$ contain the entries of $W$. Assume that, for each $m \geq 0$, there are $n$ and an ordinary Selmer cocycle $z$ for $W^*$ modulo $\ell^n$ such that $\ell^mz$ is not cohomologous to $0$ modulo $\ell^n$. Then the ordinary Selmer group of $W^*$ does not vanish.

Lean: `GlobalTheory.Ord2.gw_limit` (also `GlobalTheory.T.dualSelmer_unbounded_order_nonzero_ordinaryClass`, a second name).

*Proof.* Let $K$ be the fraction field of $\mathcal{O}$, and let $X$ be the discrete ordinary Selmer group of $W^*$ with values in $(K/\mathcal{O})^2$. It is the direct limit of the Selmer groups modulo $\ell^n$ of Section 23, under multiplication by $\ell$ on the coefficients.

We first collect the facts on $W^*$ that the argument needs. The map $W^*$ is continuous and has entries in $\mathcal{O}$, since $\varepsilon$ and $\det W = \pm 1$ have values in $\mathbb{Z}_\ell^\times$. It is upper triangular on $D_A$, because $W$ is. By the theorem of Section 20 there is $a \in \ker W$ with $\varepsilon(a) \neq 1$; then $W^*(a) = \varepsilon(a)$ has no eigenvalue $1$. So $H^0(G_S, W^*)$ is $0$ with any coefficients in which $\varepsilon(a) - 1$ is not a zero divisor, and the invariants modulo $\ell^n$ are bounded.

Step 1. The hypothesis gives elements of $X$ of unbounded order. Indeed, a Selmer cocycle $z$ modulo $\ell^n$ defines an element of $X$ through $(\mathcal{O}/\ell^n)^2 \cong (\ell^{-n}\mathcal{O}/\mathcal{O})^2$. If $\ell^mz$ is not cohomologous to $0$ modulo $\ell^n$, this element is not killed by $\ell^m$, up to a bounded factor that comes from the invariants.

Step 2. The $\ell$-torsion of $X$ is finite. It is controlled by the Selmer group of $W^*$ modulo $\ell$, which lies in the finite group $H^1(G_S, (\mathcal{O}/\ell)^2)$. This finiteness is one of the cohomological inputs.

Step 3. An $\mathcal{O}$-module that is $\ell$-primary torsion, has finite $\ell$-torsion and has elements of unbounded order contains a nonzero divisible chain: elements $x_1 \neq 0, x_2, x_3, \ldots$ with $\ell x_{k+1} = x_k$. Indeed, such a module is $(K/\mathcal{O})^r$ plus a finite group, and $r \geq 1$.

Step 4. Represent each $x_k$ by a Selmer cocycle $c_k$ modulo $\ell^k$ with integral local trivializations, chosen so that $c_{k+1} \equiv_k c_k$. Their limit $c$ is a continuous cocycle for $W^*$ with values in $\mathcal{O}^2$. It is unramified outside $\ell$ and ordinary at $A$, since the local conditions hold modulo $\ell^k$ for every $k$. If $c$ were a coboundary, then $c_1$ would be cohomologous to $0$ modulo $\ell$, so $x_1 = 0$. Hence $c$ is a nonzero ordinary Selmer class of $W^*$. $\square$

### Ordinary vanishing from the dual

**Theorem 6.24.2 (Ordinary vanishing from the dual).** Assume the cohomological inputs. Let $W$ be in normal form for $(e, S, A)$. If the ordinary Selmer group of $W^*$ vanishes, then the ordinary Selmer group of $W$ vanishes.

Lean: `GlobalTheory.Ord2.grZero_of_grZero_dual1` (also `GlobalTheory.T.ordinarySelmer_vanishes_of_dual_vanishes`, a second name).

*Proof.* Suppose that the ordinary Selmer group of $W$ does not vanish. The theorem on dual classes of unbounded order in Section 23 gives a ring $\mathcal{O}$ that contains the entries of $W$, and dual Selmer cocycles modulo $\ell^n$ of unbounded order. The previous theorem then says that the ordinary Selmer group of $W^*$ does not vanish. This contradicts the hypothesis. $\square$

The two ordinary conditions are exact annihilators of each other, so the argument is symmetric in principle. The normal form, however, is stated for $W$, and the counting of Section 23 uses it. So the chapter proves only this direction.

### The Bloch-Kato Selmer group

**Definition 6.24.3 (Bloch-Kato vanishing).** A cocycle $c$ for $W$ is a *Bloch-Kato class* if, for each prime $q \neq \ell$, there are a place $B$ over $q$ and $x$ with $c(s) = W(s)x - x$ for $s \in I_B$, and if, at each embedding of $\mathbb{Q}$ into $\overline{\mathbb{Q}}_\ell$, the restriction of $c$ to the decomposition group is a crystalline class, that is, it lies in $H^1_f$. The *Bloch-Kato Selmer group of $W$ vanishes* if every Bloch-Kato class is a coboundary.

This is the Selmer group $H^1_f(\mathbb{Q}, W)$ of S. Bloch and K. Kato, *L-functions and Tamagawa numbers of motives*, in: The Grothendieck Festschrift, Vol. I, Birkhäuser, 1990, 333 to 400, §3.

**Theorem 6.24.4 (Bloch-Kato vanishing from an Euler system class).** Assume the cohomological inputs. Let $W$ be in normal form for $(e, S, A)$, with an Euler system class at $A$ (Section 18). Then the Bloch-Kato Selmer group of $W$ vanishes.

Lean: `GlobalTheory.Ord2.es_vanish`.

*Proof.* The proof has four steps.

1. By strict vanishing (Section 22), the strict Selmer group of $W^*$ vanishes.
2. A further theorem, proved outside this chapter, upgrades this to the vanishing of the ordinary Selmer group of $W^*$. It uses the Euler system class again.
3. By the previous theorem, the ordinary Selmer group of $W$ vanishes.
4. Let $c$ be a Bloch-Kato class for $W$. Then $c$ is unramified outside $\ell$, since it is a coboundary on inertia at each $q \neq \ell$. It is also ordinary at $A$: for an ordinary representation whose sub and quotient on $D_A$ have Hodge-Tate weights $e \geq 1$ and $-e$, a crystalline class maps to $0$ in the cohomology of the quotient on inertia. This local fact comes from the local part of the cohomological inputs.

By step 3, $c$ is a coboundary. $\square$

Step 4 is the comparison between the Bloch-Kato and the Greenberg local conditions; see Greenberg, *Iwasawa theory for p-adic representations*. Here $e \geq 1$ matters: the quotient has weight $-e \neq 0$, so no unramified classes on the quotient are lost.

### Vanishing for ordinary representations of newforms

**Theorem 6.24.5 (Vanishing for an ordinary source).** Assume the cohomological inputs. Assume that every $W$ in normal form with an unramified ordinary source has an Euler system class. Let $\ell \neq 2$ and $e \geq 1$. Let $W$ be admitted for $e$: continuous, odd with $(\det W)^2 = 1$, irreducible on $H$, of finite level away from $\ell$, such that $W \otimes \varepsilon^{-e}\varphi$ is the representation of a newform of weight $2e + 1$ for a character $\varphi$ of finite order, and ordinary at a place over $\ell$ with inertia characters $\varepsilon^e\chi$ and $\varepsilon^{-e}\chi$. Assume also that $W$ has an ordinary source at $\ell$: up to twist it comes from a newform of level prime to $\ell$ whose $\ell$-th coefficient is a unit, and on each ordinary line over $\ell$ the character is not $\varepsilon$. Then the Bloch-Kato Selmer group of $W$ vanishes.

Lean: `GlobalTheory.Ord2.vanishOrdL_of_zetaUr`.

*Proof.* A theorem on normal forms gives $S$, $A$, a representation $W'$ isomorphic to $W$ by conjugation with a matrix $g$, and a newform, such that $W'$ is in normal form for $(e, S, A)$ and has an unramified ordinary source. By hypothesis $W'$ has an Euler system class at $A$. By the last theorem the Bloch-Kato Selmer group of $W'$ vanishes. This group depends only on the isomorphism class, since conjugation by $g$ carries cocycles, coboundaries and the local conditions of $W'$ to those of $W$. So the Bloch-Kato Selmer group of $W$ vanishes. $\square$

The hypothesis on Euler system classes is [the theorem on zeta classes](/entry/zeta-ur/), proved from Kato's zeta elements and [the Hodge-Tate law](/entry/k5-top/).

**Remark 6.24.6 (Formalization).** The statements with the T names are wrappers of the form `first | exact @… | …`. In the first theorem the finiteness of the $\ell$-torsion is the helper `GlobalTheory.T.finite_lTorsion_selmer_rank_two_adjoint`, whose name refers to the adjoint, but which is applied to $W^*$. The second theorem uses the normal form only to pass it on to the two theorems it combines ([OrdinarySelmerVanishesOfDualVanishes.lean](lean:Development/AbelianVarietyTheory/Proofs/FoundationProofs/OrdinarySelmerVanishesOfDualVanishes.lean#L10)). The third theorem is in a file named after the helper `localGaloisCohomology_of_galoisCohomology` at line 13, which builds the local inputs from seven of the twelve cohomological inputs ([LocPublishedOfLitCoh.lean](lean:Development/AbelianVarietyTheory/Proofs/FoundationProofs/LocPublishedOfLitCoh.lean#L16)). Its step 2 is `GlobalTheory.T.ordinarySelmer_dual_vanishes_of_strict`, a wrapper of `GlobalTheory.Ord2.Upgrade.upgrade`, and its step 4 is `GlobalTheory.T.blochKato_cocycle_unramified_and_greenbergOrdinary`. In the fourth theorem the helper `repIso_symm_srcL` only inverts the isomorphism of representations; it says nothing about sources ([VanishOrdLOfZetaUr.lean](lean:Development/AbelianVarietyTheory/Proofs/FoundationProofs/VanishOrdLOfZetaUr.lean#L13)). The transfer along the isomorphism is `UpperTheory.V.X.Kato.conj`. We read the helpers as statements; the sketches of Steps 1 to 4 of the first proof and of the local comparison are ours.

## Notes and references

The chapter builds the Galois side of Kato's method for modular forms of odd weight $2e + 1$. Part 1 constructs [a tower of modular functions](/entry/tower-ex/), proves dimension bounds, the Eichler and Shimura decomposition and semisimplicity at a newform, and realizes the [[Galois representation|JQEYEQJY2G]] of a newform in a Kummer module. It also proves the Rankin nonvanishing and the ordinary Eisenstein measure behind [the admissible functional on the tower](/entry/kato-global-admissibility-of-admissible/) and [the unit law of smoothed zeta classes](/entry/kato-global-unit-law-of-smoothed-classes/). Part 2 computes Kummer classes of Siegel units and their cup products, proves the Hodge-Tate law of zeta classes that feeds [the smoothed Hodge-Tate law](/entry/k5-top/), glues an Euler system class, and proves that such a class kills the Bloch-Kato Selmer group. The result feeds [the theorem on zeta classes](/entry/zeta-ur/) and [the vanishing of two Bloch-Kato Selmer groups](/entry/two-s/).

- G. Shimura, *Introduction to the Arithmetic Theory of Automorphic Functions*, Chapters 3, 6, 7 and 8 (Hecke operators, modular functions of higher level, the Eichler and Shimura relation, cohomology of automorphic forms; Sections 1, 3 and 16).
- P. Deligne, *Formes modulaires et représentations l-adiques*, Séminaire Bourbaki 355, Lecture Notes in Math. 179 (1971), 139 to 172 (Galois representations of newforms; Section 7).
- P. Deligne, *La conjecture de Weil. I*, Publ. Math. IHÉS 43 (1974), 273 to 307 (the bound on Hecke eigenvalues; Section 4).
- R. A. Rankin, *Contributions to the theory of Ramanujan's function τ(n) and similar arithmetical functions I*, Proc. Cambridge Philos. Soc. 35 (1939), 351 to 356 (Section 9).
- H. Hida, *Elementary Theory of L-functions and Eisenstein Series*, Chapter 7 (ordinary forms and Eisenstein measures; Sections 9 and 10).
- L. Washington, *Introduction to Cyclotomic Fields*, Chapters 7 and 12 (Gauss sums and $p$-adic measures; Section 19).
- R. Coleman, *Division values in local fields*, Invent. Math. 53 (1979), 91 to 116 (Coleman power series; Sections 17 to 19).
- S. Lang, *Elliptic Functions*, Chapter 5 (the modular equation and the Kronecker congruence; Section 16).
- J. Tate, *p-divisible groups*, in: Proceedings of a Conference on Local Fields, Springer, 1967, 158 to 183 (Hodge-Tate decomposition; Sections 13 and 17).
- J.-M. Fontaine, *Formes différentielles et modules de Tate des variétés abéliennes sur les corps locaux*, Invent. Math. 65 (1982), 379 to 409 (differentials of $\overline{\mathbb{Z}}_p$; Section 13).
- I. Fesenko and S. Vostokov, *Local Fields and Their Extensions*, Chapter VII (explicit reciprocity; Section 17).
- K. Kato, *p-adic Hodge theory and values of zeta functions of modular forms*, Astérisque 295 (2004), 117 to 290 (Siegel units, zeta elements and the method of the whole chapter).
- K. Rubin, *Euler Systems*, Chapters 2, 4 and 5 (Euler systems and the Kolyvagin argument; Sections 18, 21 and 22).
- J. S. Milne, *Arithmetic Duality Theorems*, Chapter I, and J. Neukirch, A. Schmidt and K. Wingberg, *Cohomology of Number Fields*, Chapters VII and VIII (local and global duality; Sections 21 to 23).
- R. Greenberg, *Iwasawa theory for p-adic representations*, in: Algebraic Number Theory, Adv. Stud. Pure Math. 17 (1989), 97 to 137 (ordinary Selmer conditions; Sections 22 and 24).
- A. Wiles, *Modular elliptic curves and Fermat's Last Theorem*, Ann. of Math. 141 (1995), 443 to 551, and H. Darmon, F. Diamond and R. Taylor, *Fermat's Last Theorem*, Theorem 2.19 (the Greenberg and Wiles formula; Section 23).
- S. Bloch and K. Kato, *L-functions and Tamagawa numbers of motives*, in: The Grothendieck Festschrift, Vol. I, Birkhäuser, 1990, 333 to 400 (the Bloch-Kato Selmer group; Section 24).

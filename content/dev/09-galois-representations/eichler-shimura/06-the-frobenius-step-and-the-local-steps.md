---
title: The Frobenius step and the local steps
decls:
  - UpperTheory.Gal.Int.Geo.geoSide_of
  - UpperTheory.Gal.Int.Geo.steps_of
  - UpperTheory.Gal.Int.Geo.steps_holds
status: drafted
drafted_by: writer@claude-opus-5-5
---
## The Frobenius step and the local steps

At a place $w \mid \ell$ the Eichler-Shimura relation of [the second section](/entry/es-step-holds/) has a crystalline form. The Galois piece is crystalline there by [the crystalline step](/entry/crys-step-holds/), so it has a module $D_{\mathrm{cris}}$ with a Frobenius $\varphi$. If the tower has a congruence model at $w$, the Hecke polynomial kills the linear Frobenius $\varphi^f$ on $D_{\mathrm{cris}}$ of the piece. This section proves that statement, deduces the Frobenius step from it, and then collects all the local steps of the chapter in one list.

Throughout, $E$ is a number field, $\Omega$ an algebraic closure, $\ell$ a prime, and $H$ a nice Hecke tower over $E$ with $\theta : \Gamma \to \overline{\mathbb{Q}}_\ell$. For a place $w$ of $E$ above $\ell$, we fix a place of $\Omega$ above $w$, the completion $E_w \subset \overline{\mathbb{Q}}_\ell$, and an identification of the decomposition group with $G_{E_w}$. We write $f$ for the residue degree of $w$, so $N(w) = \ell^f$. We use the [period ring](/learn/galois-representations/#period-rings) $B_{\mathrm{cris}}$ with its Frobenius $\varphi$, and for a representation $V$ of $G_{E_w}$ we write $D_{\mathrm{cris}}(V) = (V \otimes_{\mathbb{Q}_\ell} B_{\mathrm{cris}})^{G_{E_w}}$.

**Theorem 3.6.1 (crystalline Eichler-Shimura relation).** Assume the crystalline Hecke relation (Theorem 3.6.2 below) and the [crystalline comparison theorem](/entry/crys-step-of/). Let $\rho_0 : \operatorname{Gal}(\Omega/E) \to \mathrm{GL}_a(\overline{\mathbb{Q}}_\ell)$ be a matrix form of $\Pi_\theta$. Let $w$ be a place of $E$ above $\ell$, and suppose that $(H, \theta)$ has a congruence model at $w$ with data $(n, \vartheta)$. Then there are a finite-dimensional crystalline $\mathbb{Q}_\ell$-representation $V$ of $G_{E_w}$, endomorphisms $T_0, \dots, T_n$ of $V$, and an injective $\overline{\mathbb{Q}}_\ell$-linear map $b : \overline{\mathbb{Q}}_\ell^{\,a} \to \overline{\mathbb{Q}}_\ell \otimes V$ such that:

1. $b(\rho_0(\sigma) x) = \sigma\, b(x)$ for all $\sigma \in G_{E_w}$ and all $x$;
2. $T_j\, b(x) = \vartheta_j\, b(x)$ for all $j \leq n$ and all $x$;
3. on $D_{\mathrm{cris}}(V)$, with $q = N(w)$,
$$\sum_{j=0}^{n} (-1)^j q^{\binom{j}{2}}\, \bigl(T_j \otimes \varphi^{f(n-j)}\bigr) = 0.$$

Lean: `UpperTheory.Gal.Int.Geo.geoSide_of`.

So the piece sits inside a crystalline representation on which $P_{q,n,\vartheta}(\varphi^f) = 0$, with the [Hecke polynomial](/entry/es-step-holds/) $P_{q,n,\vartheta}$. The first input is the following statement, which is proved in [another chapter](/entry/fin-all/).

**Theorem 3.6.2 (crystalline Hecke relation on a smooth model).** Let $K \subset \overline{\mathbb{Q}}_\ell$ be a finite extension of $\mathbb{Q}_\ell$ with residue field of order $\ell^f$, $f > 0$, let $\varpi$ be a uniformizer, and let $Y$ be a projective scheme over $\mathcal{O}_K$ that is strictly semistable for some uniformizer and smooth. Let $T_0, \dots, T_n$ be correspondences on $Y$ that satisfy the zero-cycle identity of [the congruence relation](/entry/es-step-holds/) on the special fibre with $q = \ell^f$, and let $A_i$ be the action of $T_i$ on $V_j = H^j(Y_{\overline{\mathbb{Q}}_\ell}, \mathbb{Q}_\ell)$. Then there is $N \geq 0$ such that for every $x \in D_{\mathrm{cris}}(V_j)$
$$\sum_{i=0}^{n} (-1)^i q^{\binom{i}{2}}\, \bigl(A_i \otimes \varphi^{f(n-i+N)}\bigr)(x) = 0.$$

Lean: `UpperTheory.Gal.crystallineComparison.Br.FinAll` (the statement).

This is the crystalline analogue of the Eichler-Shimura theorem on a good model. Its standard source is the compatibility of the crystalline comparison isomorphism $D_{\mathrm{cris}}(V_j) \cong H^j_{\mathrm{cris}}(Y_{\kappa}/W(\kappa))[1/\ell]$ with Frobenius and with correspondences (G. Faltings, Crystalline cohomology and $p$-adic Galois representations, 1989), together with the fact that the crystalline Frobenius of the special fibre is induced by the $q$-power map.

*Proof of the crystalline Eichler-Shimura relation.* First, pass to the completion. The congruence model over $O_w$ gives, by base change along $O_w \to \mathcal{O}_{E_w}$, an onto good model over $\mathcal{O}_{E_w}$ with the congruence relation for the same data. The prime $p$ of the congruence model lies under $w$, and $\ell$ also lies under $w$, so $p = \ell$ and $q = N(w) = \ell^f$. The restriction of $\rho_0$ to the decomposition group is a matrix form $\rho_1$ of the piece of the base changed tower.

Second, embed the piece. As in the proof that [the piece embeds in the model](/entry/mat-in-holds/), the pullback along $Z \to Y$ is injective on cohomology, and its image contains $\Pi_\theta$. So for some $N'$ there is an injective Galois equivariant map $b$ from $\overline{\mathbb{Q}}_\ell^{\,a}$ with the action $\rho_1$ into $\overline{\mathbb{Q}}_\ell \otimes V$, where $V = \bigoplus_{j < N'} V_j$.

Third, compare the Hecke operators. The correspondence $T_i$ lies under $\gamma_i \in \Gamma$ with degree $m_i$. So on the image of the pullback, the Hecke operator of $\gamma_i$ is $m_i$ times the pullback of the action $A_i$ of $T_i$. On $\Pi_\theta$ the Hecke operator of $\gamma_i$ is $\theta(\gamma_i) = m_i \vartheta_i$. Since $m_i > 0$ and we are in characteristic $0$, $A_i$ acts on the image of $b$ by $\vartheta_i$. This gives property 2 with $T_i = \bigoplus_j A_i$.

Fourth, each $V_j$ is crystalline by the comparison theorem, so $V$ is crystalline. By the crystalline Hecke relation there is $N$ such that $\sum_i (-1)^i q^{\binom{i}{2}} (A_i \otimes \varphi^{f(n-i+N)}) = 0$ on $D_{\mathrm{cris}}(V)$. The operator $\varphi$ is bijective on $D_{\mathrm{cris}}(V)$, and it commutes with each $A_i \otimes 1$. Apply $\varphi^{-fN}$ to get property 3. $\square$

**Theorem 3.6.3 (Frobenius step).** Let $\iota : \overline{\mathbb{Q}}_\ell \cong \mathbb{C}$, and let $\rho$ be a continuous Galois piece of $(H, \theta)$. Let $w$ be a place above $\ell$ where $(H, \theta)$ has a congruence model with data $(n, \vartheta)$. Suppose $\vartheta_0 \neq 0$ and $\iota\, P_{N(w), n, \vartheta} = \iota(\vartheta_0)\, \operatorname{root}_R$ for a multiset $R$ in $\mathbb{C}$. Then the restriction of $\rho$ to the decomposition group is crystalline, and its [Weil-Deligne representation](/learn/galois-representations/#the-weil-group) has a geometric Frobenius element $g$ whose characteristic polynomial divides $\operatorname{root}_R^{\,m}$ for some $m$.

Lean: `UpperTheory.Gal.Int.Geo.PhiStep` (the statement; it is proved as [Theorem 3.10.6 of Volume 3](/entry/phi-step/) from the crystalline Eichler-Shimura relation by [Theorem 3.10.9 of Volume 3](/entry/phi-step-of/)).

The proof in the other chapter passes from the crystalline representation $V$ to a model over a finite extension of $\mathbb{Q}_\ell$, uses that the Hecke polynomial is then nilpotent on $D_{\mathrm{cris}}$ of the graded part, and reads the Weil-Deligne Frobenius off $\varphi^f$ (J.-M. Fontaine, Représentations $\ell$-adiques potentiellement semi-stables, Astérisque 223 (1994)). In the notation of [Volume 1](/learn/galois-representations/#decomposition-groups-inertia-and-frobenius), an element of degree $-1$ of the Weil group acts on the residue field by $x \mapsto x^{1/q}$, so it is a geometric Frobenius.

**Definition 3.6.4 (the local steps).** The *local steps* are the following seventeen statements, for all number fields $E$, primes $\ell$, isomorphisms $\iota$, nice towers $H$ and functions $\theta$.

1. Galois pieces exist ([Theorem 3.1.6](/entry/rep-ex-holds/)).
2. The Eichler-Shimura step at $w \nmid \ell$ ([Theorem 3.2.6](/entry/es-step-holds/)).
3. The crystalline step at $w \mid \ell$ ([Theorem 3.3.4](/entry/crys-step-holds/)).
4. The Hodge-Tate jump step at $w \mid \ell$ ([Theorem 3.5.3](/entry/jump-step-holds/)).
5. The Frobenius step at $w \mid \ell$ (above).
6. If $(H, \theta)$ has a good model or a congruence model at $w$, then it has one that is onto.
7. to 10. Twisting by a continuous character $\chi$ with a Frobenius value $c$ at $w$ and Hodge-Tate weights $m$ preserves the four local conclusions: the Eichler-Shimura roots are multiplied by $c$, crystallinity is kept, the Hodge-Tate jumps are shifted by $m$, and the Frobenius roots are multiplied by $c$.
11. to 14. Four statements that translate the local conclusions into the language of automorphic weights and Satake parameters of the next part of the chapter: the Frobenius step for a saturated root list, the size of a Satake list, the jumps given by the weights, and the abundance of Hodge-Tate weights at a place with lacunary weights.
15. Every algebraic Hecke character of $E$ has a continuous $\ell$-adic Galois character with the expected Frobenius values and Hodge-Tate weights (A. Weil, On a certain type of characters of the idèle-class group, 1956; J.-P. Serre, *Abelian $\ell$-adic Representations*, Chapter II).
16. and 17. Semisimplicity and continuity pass to direct summands, to isomorphic representations and to twists by characters, and a continuous character gives a continuous representation of rank one.

Lean: `UpperTheory.Gal.Int.Geo.Steps`.

**Theorem 3.6.5 (the local steps hold).** Assume the crystalline step, the Hodge-Tate jump step and the Frobenius step (items 3, 4 and 5). Then the seventeen local steps hold.

Lean: `UpperTheory.Gal.Int.Geo.steps_of` (also `UpperTheory.Gal.Int.Geo.steps_holds`, the same statement with the three steps supplied).

*Proof.* Items 1 and 2 are the theorems of the first two sections. Items 3, 4 and 5 are the hypotheses. Items 6 to 17 are proved elsewhere in the Handbook and are cited here. To get the unconditional form, supply item 3 by [the crystalline step](/entry/crys-step-holds/), item 4 by [the jump step](/entry/jump-step-holds/), and item 5 by [the Frobenius step](/entry/phi-step/). $\square$

**Remark 3.6.6.** The conclusion of the Frobenius step is a divisibility: the characteristic polynomial of one geometric Frobenius divides a power of $\operatorname{root}_R$. So every Frobenius eigenvalue lies in $R$, but multiplicities are not compared. Theorem 3.6.2 has $\varphi^{f(n-i+N)}$ with an extra $N$; the proof of Theorem 3.6.1 removes $N$ by the bijectivity of $\varphi$ on $D_{\mathrm{cris}}$.

**Remark 3.6.7 (Formalization).** The conclusion of Theorem 3.6.1 is `UpperTheory.Ru.crystallineComparison.InCrys`, with the annihilation `UpperTheory.Gal.crystallineComparison.AnnD`, and that of Theorem 3.6.3 is `PhiK`. `UpperTheory.Gal.Int.Geo.geoSide_of` is built from `UpperTheory.Ru.crystallineComparison.congBC` (pass to the completion, $p = \ell$), `UpperTheory.Gal.Seam.locTower_holds` (restrict the matrix form) and `UpperTheory.Ru.crystallineComparison.geoLoc` (the local statement). The Frobenius step is `UpperTheory.Ru.crystallineComparison.phiStep`, which applies `geoSide_of` to `UpperTheory.Ru.crystallineComparison.finAll` and `UpperTheory.Ru.crystallineComparison.smoothModel_crystalline`. The record `UpperTheory.Gal.Int.Geo.Steps` is the only interface between this part of the chapter and [the next section](/entry/geo-one-holds/). Items 11 to 14 are `UpperTheory.Gal.Int.Geo.PhiOf`, `SatCard`, `JumpsOf` and `RichOf`, described here only by their role.

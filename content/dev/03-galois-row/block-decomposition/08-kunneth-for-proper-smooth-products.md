---
title: Künneth for proper smooth products
decls:
  - GlobalTheory.T.kuenneth_product_proper_smooth
  - GlobalTheory.CompanionTheory.KunGlue.kun_left
  - GlobalTheory.CompanionTheory.KunGlue.slantOf
status: drafted
drafted_by: writer@claude-opus-5-5
---
## Künneth for proper smooth products

Let $X$ and $X'$ be proper smooth schemes over a field $K$ of characteristic $0$. This section proves a Künneth formula for the Hodge cohomology of $X \times_K X'$ on the thickening site. The proof covers $X$ by finitely many opens with coordinates, uses a local Künneth formula on each finite intersection, and glues with [the Mayer-Vietoris argument](/entry/pairing-restriction-natural/) of the previous section. As a consequence, every linear form on a Hodge cohomology group of $X$ gives a *slant map* from the cohomology of the product to the cohomology of $X'$. The slant maps are one of the [parts of the Hodge-Tate comparison](/entry/parts/).

We use the site of thickenings of [the chapter on the $\ell$-adic Hodge comparison](/entry/hodge-affine-iso-sign/), over $K$ with the zero divided power ideal. For a scheme $Z$ that is [[smooth|EXKGG9X6J0]] over $K$ and an open $V \subseteq Z$, write $\mathcal{T}(Z)$ for the category of thickenings of $Z$ and $\mathcal{T}(V) \subseteq \mathcal{T}(Z)$ for the full subcategory of thickenings whose point lies in $V$. The structure functor carries the divided power filtration $J^{[a]}$, with graded pieces $\operatorname{gr}^a = J^{[a]} / J^{[a+1]}$.

**Definition 8.8.1 (Hodge cohomology on the thickening site).** For $a, i \geq 0$ and an open $V \subseteq Z$, put
$$H^{a, i}(V) = H^i\bigl(C^\bullet(\mathcal{T}(V), \operatorname{gr}^a)\bigr),$$
the cohomology of the cochain complex of the functor $\operatorname{gr}^a$ on $\mathcal{T}(V)$. Write $H^{a,i}(Z)$ for $V = Z$.

On an open with coordinates, $H^{a,i}$ is $0$ for $i \neq a$, and $H^{a,a}$ is the space of [[Kähler differential|7HCFARHG7D]] $a$-forms. This is one of the hypotheses below. So $H^{a,i}(Z)$ plays the role of $H^{i-a}(Z, \Omega^a)$.

**Definition 8.8.2 (The cup product of a product).** Let $P = X \times_K X'$ with projections $p_1$ and $p_2$. A thickening of $P$ gives, through $p_1$ and $p_2$, thickenings of $X$ and of $X'$. So cochains on $\mathcal{T}(X)$ and on $\mathcal{T}(X')$ pull back to cochains on $\mathcal{T}(P)$. The product $\operatorname{gr}^a \times \operatorname{gr}^{a'} \to \operatorname{gr}^{a + a'}$ on $P$ and the cup product of cochains give a pairing of complexes
$$C^\bullet(\mathcal{T}(U_1), \operatorname{gr}^a) \times C^\bullet(\mathcal{T}(U_2), \operatorname{gr}^{a'}) \to C^\bullet(\mathcal{T}(U_3), \operatorname{gr}^{a + a'}), \qquad (x, y) \mapsto p_1^* x \cup p_2^* y,$$
for opens $U_1 \subseteq X$, $U_2 \subseteq X'$ and $U_3 \subseteq p_1^{-1} U_1 \cap p_2^{-1} U_2$.

**Theorem 8.8.3 (Künneth for proper smooth products).** Let $K$ be a field of characteristic $0$, $X$ and $X'$ proper and smooth over $K$, and $P = X \times_K X'$. Assume the six hypotheses listed in the remark below. Then for all $c, n \geq 0$ there is an isomorphism
$$\bigoplus_{a + a' = c} \; \bigoplus_{i + j = n} H^{a, i}(X) \otimes_K H^{a', j}(X') \xrightarrow{\ \sim\ } H^{c, n}(P)$$
that sends $[x] \otimes [y]$ to $[p_1^* x \cup p_2^* y]$.

Lean: `GlobalTheory.T.kuenneth_product_proper_smooth` (also `GlobalTheory.CompanionTheory.KunGlue.kun_left`, the same statement).

The classical analogue is the Künneth formula for Hodge cohomology, $H^m(X \times X', \Omega^c) \cong \bigoplus H^{m'}(X, \Omega^a) \otimes H^{m''}(X', \Omega^{a'})$, which follows from the decomposition of $\Omega^c$ of a product and the Künneth formula for coherent cohomology.

**Remark 8.8.4.** The Lean statement takes six propositions as hypotheses, each about the thickening site:

1. *Site laws:* the subcategories $\mathcal{T}(V)$ are cosieves, $\mathcal{T}(Z)$ is everything, $\mathcal{T}(V \cap V') = \mathcal{T}(V) \cap \mathcal{T}(V')$, and $\mathcal{T}(u^{-1} V)$ is the inverse image of $\mathcal{T}(V)$ under a morphism $u$. Two more laws, on thickenings whose point factors through a given morphism, are not used here.
2. *The Mayer-Vietoris principle* of the previous section.
3. *Covering descent* of the previous section.
4. *Zariski invariance:* if the opens $U_s$ cover $V$, the restriction from $\mathcal{T}(V)$ to the union of the $\mathcal{T}(U_s)$ is bijective on the cohomology of each $\operatorname{gr}^a$.
5. *Affine computation:* on an open with coordinates, $H^{a,j} = 0$ for $j \neq a$ and $H^{a,a}$ is the space of $a$-forms.
6. *Affine Künneth:* for opens $V \subseteq X$ and $V' \subseteq X'$ with coordinates, $p_1^{-1} V \cap p_2^{-1} V'$ has coordinates, and the cup product gives an isomorphism $\bigoplus_{a} H^{a,a}(V) \otimes H^{c-a, c-a}(V') \cong H^{c,c}(p_1^{-1} V \cap p_2^{-1} V')$.

They are stated in the Lean code as `SiteLaws`, `MVBij`, `CovDesc`, `ZarAbs`, `AffOm` and `KunAff`. This section does not prove them.

The proof needs one more input, which we take from another statement of the folder.

**Lemma 8.8.5 (Coordinate open times a proper smooth scheme).** Under the same six hypotheses, let $X$ be any scheme over $K$ and $V \subseteq X$ an open with coordinates. Let $X'$ be proper and smooth over $K$. Then the Künneth isomorphism holds for $\mathcal{T}(V)$, $\mathcal{T}(X')$ and $\mathcal{T}(p_1^{-1} V)$.

Lean: `GlobalTheory.T.kuenneth_product_local_global`.

We have read the statement of this lemma, not its proof.

*Proof of the theorem.*

1. *A cover.* A proper morphism is separated and quasi-compact. So $X$ has a finite cover by opens $U_s$, $s \in \iota$, with coordinates, such that every nonempty finite intersection $U_S = \bigcap_{s \in S} U_s$ is affine. This is a lemma of the code on smooth coordinate covers.
2. *Two families of cosieves.* Let $V_s = \mathcal{T}(U_s)$ in $\mathcal{T}(X)$ and $W_s = \mathcal{T}(p_1^{-1} U_s)$ in $\mathcal{T}(P)$. By the site laws these are cosieves, and for $S$ nonempty $V_S = \mathcal{T}(U_S)$ and $W_S = \mathcal{T}(p_1^{-1} U_S)$. A thickening in $W_S$ maps under $p_1$ to a thickening in $V_S$, so the pairing of cochains is defined for each $S$.
3. *The local case.* Let $S$ be nonempty and $s_0 \in S$. The open $U_S$ is affine and lies in $U_{s_0}$, so the coordinates of $U_{s_0}$ restrict to coordinates on $U_S$. The lemma on a coordinate open times a proper smooth scheme gives the Künneth isomorphism for $V_S$, $\mathcal{T}(X')$ and $W_S$.
4. *Gluing.* The theorem on Künneth on a union of cosieves, with the two factors swapped, gives the Künneth isomorphism for the unions $V_\emptyset = \bigcup_s \mathcal{T}(U_s)$ and $W_\emptyset = \bigcup_s \mathcal{T}(p_1^{-1} U_s)$, with $\mathcal{T}(X')$ as the fixed factor.
5. *From the unions to the whole.* The $U_s$ cover $X$ and the $p_1^{-1} U_s$ cover $P$. By Zariski invariance, the restrictions $\mathcal{T}(X) \supseteq V_\emptyset$ and $\mathcal{T}(P) \supseteq W_\emptyset$ are bijective on the cohomology of each $\operatorname{gr}^a$. A transfer lemma of the folder moves the Künneth isomorphism along bijective restrictions. $\square$

**Remark 8.8.6.** The properness and smoothness of $X$ are used only in step 1, to get the finite cover by opens with coordinates. The properness and smoothness of $X'$ are passed on to the local lemma of step 3. Characteristic $0$ is also only passed on. The statement in Lean is phrased with the open $p_1^{-1}(X) \cap p_2^{-1}(X')$ of $P$, which is all of $P$, and with two inclusion hypotheses that are always true. The theorem under the name `kuenneth_product_proper_smooth` is proved by a single `first | exact` that cites the companion theorem ([KuennethProductProperSmoothStatement.lean](lean:Development/AutomorphicSpectrum/Proofs/BlockDecomposition/KuennethProductProperSmoothStatement.lean#L11)). The gluing step uses a fixed second factor, so the previous section is applied to the pairing with the two factors swapped, which multiplies the pairing by $(-1)^{ij}$ in degrees $i$ and $j$.

We now derive the slant maps.

**Theorem 8.8.7 (Slant maps).** Let $K$, $X$, $X'$ and $P$ be as in the Künneth theorem, and assume the same six hypotheses together with the restriction law below. Let $a + a' = c$, $i + j = n$, and let $\varphi$ be a linear form on $H^{a, i}(X)$. Then there is a linear map
$$\operatorname{sl}_\varphi : H^{c, n}(P) \to H^{a', j}(X')$$
such that $\operatorname{sl}_\varphi(p_1^* u \cup p_2^* v) = \varphi(u) \, v$ for $u \in H^{a, i}(X)$ and $v \in H^{a', j}(X')$, and $\operatorname{sl}_\varphi(p_1^* u \cup p_2^* v) = 0$ for $u \in H^{b, i'}(X)$ and $v \in H^{b', j'}(X')$ with $b + b' = c$, $i' + j' = n$ and $(b, i') \neq (a, i)$.

Lean: `GlobalTheory.CompanionTheory.KunGlue.slantOf`.

**Definition 8.8.8 (Restriction law).** The *restriction law* says: for a functor $F$ on a category $\mathcal{C}$ and a full subcategory $U$ that contains every object, restriction of cochains from $\mathcal{C}$ to $U$ is bijective in each degree, and a cochain vanishes on the chains that start in a given full subcategory if and only if its restriction does.

Lean: `CrystallineSemistableComparison.Onto.TopRes` (a proposition, used as a hypothesis).

*Proof.*

1. *Künneth on the whole site.* The cup product in the statement is defined on the cohomology of the whole category $\mathcal{T}(Z)$. The Künneth theorem is stated on the full subcategories $\mathcal{T}(X)$, $\mathcal{T}(X')$ and $\mathcal{T}(P)$ for the open that is the whole scheme. By the site laws these contain every object. The restriction law identifies their cohomology with the cohomology of the whole category, compatibly with the cup product.
2. *The slant map.* Under the Künneth isomorphism, $H^{c,n}(P)$ is a direct sum of the spaces $H^{b, i'}(X) \otimes H^{b', j'}(X')$. Define $\operatorname{sl}_\varphi$ as $\varphi \otimes \mathrm{id}$ on the summand of $(a, i, a', j)$, followed by $K \otimes H^{a', j}(X') = H^{a', j}(X')$, and as $0$ on every other summand.
3. *The two formulas.* The class $p_1^* u \cup p_2^* v$ is the image of $u \otimes v$ in the summand of $(b, i', b', j')$. On the summand of $(a, i, a', j)$ the map gives $\varphi(u) v$. On the other summands it gives $0$. $\square$

**Remark 8.8.9.** In Lean the slant theorem is the implication from the restriction law to the proposition `SlantOf`, which is itself the implication from the six hypotheses to the slant statement. The proof composes a lemma that derives slant maps from the Künneth isomorphism for all proper smooth pairs (Lean: `GlobalTheory.T.slant_of_hodge_kuenneth`) with the Künneth theorem of this section. That lemma is proved in [KuennethIsoProperSmooth.lean](lean:Development/AutomorphicSpectrum/Proofs/BlockDecomposition/KuennethIsoProperSmooth.lean#L120), a file whose name speaks of the Künneth isomorphism while it holds the slant maps. Only the summand of $(a, i, a', j)$ needs the form $\varphi$, and steps 2 and 3 use no property of $\varphi$ other than linearity.

## Notes and references

This chapter collects the results of the folder `BlockDecomposition` that feed [the Galois row](/proof/galois-row/). The folder name does not describe them: they are inputs to the $\ell$-adic Hodge comparison. The level lattice feeds the result that [each level is good](/entry/lev-good/) and through it [the existence of the level system](/entry/lev-sys-ex/). The continuous functions on $\mathbb{Z}_\ell$ give the line object, which is [the continuous line](/entry/cont-line/) of the [local comparison](/entry/local-of/). The relative forms on blow-up charts and the slant maps are [parts of the Hodge-Tate comparison](/entry/parts/), which give [the bijectivity of the Hodge-Tate map](/entry/ht-bij-of/). The vanishing on affine opens is [the input of the same name](/entry/gr-aff-pf/) of the step [GeoOne holds](/step/geo-one-holds/). The cone transfer is [the transfer lemma](/entry/cone-transfer/) in the proof that [the top power of the first Chern class is nonzero](/entry/pow-k-ne-zero-of/).

Sources:

- R. Bott and L. W. Tu, *Differential Forms in Algebraic Topology*, Graduate Texts in Mathematics 82, Springer, 1982. Chapter I, §5 gives the Mayer-Vietoris argument for the Künneth formula.
- R. Hartshorne, *Algebraic Geometry*, Graduate Texts in Mathematics 52, Springer, 1977. Chapter III, §3 and §4 give the vanishing of quasi-coherent cohomology on affine schemes and Čech cohomology.
- P. Berthelot and A. Ogus, *Notes on Crystalline Cohomology*, Princeton University Press, 1978. Section 3 treats divided powers.
- J.-M. Fontaine, Le corps des périodes $p$-adiques, in *Périodes $p$-adiques*, Astérisque 223, 1994, Exposé II. It constructs the period rings $B_{\mathrm{dR}}^+$ and $A_{\mathrm{cris}}$ used in the sections on the level lattice and the continuous line.
- O. Brinon and B. Conrad, *CMI Summer School notes on $p$-adic Hodge theory*, 2009. They give an introduction to the [period rings](/learn/galois-representations/#period-rings).

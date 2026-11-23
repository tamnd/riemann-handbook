---
title: A Breuil-Kisin pack for a good lattice
decls:
  - GlobalTheory.BKGal.exists_pack_isOfType
  - GlobalTheory.T.exists_breuilKisinModule_tameDescent_goodLattice
status: drafted
drafted_by: writer@claude-opus-5-5
---
## A Breuil-Kisin pack for a good lattice

This section attaches to each good lattice of $G_{\mathbb{Q}_\ell}$ a Breuil-Kisin module with all the structure that the lifting argument needs: a descent datum for the tame Galois group, an integral connection, height bounds, and a comparison with the lattice through crystalline periods. It also shows that the characters of the descent datum and the jumps of the module are those that the good lattice prescribes. The construction collects the results of the three previous sections. It is used in the next section, once for each lattice of a short exact sequence.

We keep the notation of [the integral connection](/entry/int-conn-taylor-main/) and [the monodromy](/entry/jumps-of-m-main/): $\ell \ne 2$ is a prime, $e + 1 = \ell^a$, $\varpi$ is a system of roots, $K_\varpi$ is the tame field, and $L$ is a finite extension of $\mathbb{Q}_\ell$ with ring of integers $\mathcal{O}$ that contains the unramified field of degree $a$, with tame descent data. Fix standard period data for $\mathbb{Q}_\ell$. Let $\omega : I_{\mathbb{Q}_\ell} \to L^\times$ be the tame character of level $e$: for $g \in I_{\mathbb{Q}_\ell}$, $\omega(g)$ is the element with $g(\varpi_0) = \omega(g)\, \varpi_0$.

**Definition 7.14.1 (Good lattice).** Let $\Sigma \subseteq \mathbb{Z}/e$ and $U \subseteq \mathbb{Z}$ be finite sets. An $\mathcal{O}$-lattice $T$ of $G_{\mathbb{Q}_\ell}$, in the representation $V$, is *good* for $(\Sigma, U)$ if:

1. the restriction of $V$ to $G_{K_\varpi}$ is crystalline;
2. $T$ has *tame type* $\Sigma$: for every $g \in I_{\mathbb{Q}_\ell}$ and every $x \in D_{\mathrm{cris}}(V|_{G_{K_\varpi}})$,
$$\prod_{c \in \Sigma} \big(g - \omega(g)^c\big)\, x = 0 \quad \text{in } V \otimes B_{\mathrm{cris}};$$
3. every Hodge-Tate jump of $V$ lies in $U$.

So $V$ becomes crystalline over the tame field, the inertia group acts on $D_{\mathrm{cris}}$ over $K_\varpi$ through powers $\omega^c$ with $c \in \Sigma$, and the Hodge-Tate weights lie in $U$.

The tame Galois group acts on the Breuil-Kisin ring: an element $\gamma$ shifts the index $\tau$ and scales $X$ by a root of unity. We write $\gamma \cdot f$ for this action on families $f = (f_\tau)$ of series.

**Definition 7.14.2 (Descent datum).** A *descent datum* on a $\varphi$-module $P$ is a representation $\Delta$ of the tame Galois group on vectors that is semilinear, $\Delta(\gamma)(f v) = (\gamma \cdot f)\, \Delta(\gamma)(v)$, that preserves the lattice $M$, and that commutes with $\varphi$. Its *characters* at $\tau$ are the characters of the tame inertia that occur in it at the place $\tau$ (we do not unfold them).

**Definition 7.14.3 (Breuil-Kisin datum).** Let $\eta, H \ge 0$. A *Breuil-Kisin datum* of heights $(\eta, H)$ is a $\varphi$-module $P$ with lattice $M$ and image lattice $\varphi^* M$, the $\mathfrak{S}_{\mathcal{O}}$-span of the columns of the $Y_\tau$, together with:

1. a descent datum $\Delta$;
2. the condition that $\nabla_P$ preserves the divided power lattice $\mathcal{M}$;
3. the condition $E N(M) \subseteq M_R$;
4. the height conditions $E^H M \subseteq \varphi^* M$ and $E^\eta \varphi^* M \subseteq M$.

Part 4 says that $E^\eta Y_\tau$ and $E^H Y_\tau^{-1}$ have entries in $\mathfrak{S}_{\mathcal{O}}$.

**Definition 7.14.4 (Galois datum and pack).** A *Galois datum* for a Breuil-Kisin datum $D$ and a lattice $T$ of $G_{\mathbb{Q}_\ell}$ consists of an identification $j$ of $P$ with $T$ and a crystalline comparison $j_B$ for $(P, j)$, such that the descent datum is compatible with the Galois action through $j$, and $G_{\mathbb{Q}_\ell}$ preserves the image of the integral lattice of $P$ under $j$. A *pack* of heights $(\eta, H)$ for $T$ is a rank $n$, a Breuil-Kisin datum $D$ of rank $n$ and heights $(\eta, H)$, a Galois datum for $(D, T)$, and the condition that the restriction of $j$ to $G_{K_\varpi}$ comes from a prismatic F-crystal. The pack is *of type* $(\Sigma, U)$ if the characters of $\Delta$ at every $\tau$ lie in $\Sigma$ and the jumps of $P$ lie in $U$.

**Theorem 7.14.5 (Packs for good lattices).** Assume the theorem of Bhatt and Scholze on crystalline lattices and the theorem of Fontaine. Let $\ell \ne 2$, $\eta, H \ge 0$, $\Sigma \subseteq \mathbb{Z}/e$ finite, and $U \subseteq \mathbb{Z}$ finite with $-\eta \le i \le H$ for every $i \in U$. Let $T$ be an $\mathcal{O}$-lattice of $G_{\mathbb{Q}_\ell}$ that is good for $(\Sigma, U)$. Then $T$ has a pack of heights $(\eta, H)$ of type $(\Sigma, U)$.

Lean: `GlobalTheory.BKGal.exists_pack_isOfType` (also `GlobalTheory.T.exists_breuilKisinModule_tameDescent_goodLattice`, a second name).

*Proof.* *Step 1: the Breuil-Kisin module.* The theorem of Bhatt and Scholze gives a functor from crystalline lattices of $G_{K_\varpi}$ over $\mathcal{O}$ to Breuil-Kisin modules: each lattice goes to a $\varphi$-module $P$ of some rank $n$ with an identification that comes from a prismatic F-crystal. Apply it to the restriction of $T$ to $G_{K_\varpi}$, which is crystalline since $T$ is good. This gives $n$, $P$ and an identification $j$ of $P$ with $T$; the identification is defined over $G_{K_\varpi}$, and as a map of modules it is also an identification for $T$ over $G_{\mathbb{Q}_\ell}$.

*Step 2: the connection.* By [the integral connection and Taylor formula](/entry/int-conn-taylor-main/), $\nabla_P$ preserves $\mathcal{M}$, and $(j, \nabla_P)$ has the Taylor property.

*Step 3: the comparison.* A lemma on Breuil-Kisin modules gives a $B_{\mathcal{O}}$-linear isomorphism $j_B$ that agrees with $j$ on integral periods. With the Taylor property of Step 2, a second lemma shows that $G_{K_\varpi}$ fixes $j_B(\xi(d))$ for every horizontal vector $\xi(d)$ in the divided power lattice. So $j_B$ is a crystalline comparison.

*Step 4: the descent datum.* The image of $M$ under $j$, tensored up to $A_{\inf}$, is stable under $G_{K_\varpi}$, and the Kummer tower fixes the image of $M$ itself. Then the theorem of Bhatt and Scholze shows that the Galois group of the Kummer tower preserves the Breuil-Kisin module. From these facts, a descent lemma gives a descent datum $\Delta$ on $P$ that is compatible with the Galois action through $j$, and it gives that $G_{\mathbb{Q}_\ell}$ preserves the integral lattice.

*Step 5: monodromy and jumps.* By [the theorem on monodromy and jumps](/entry/enstable-and-jumps/), with the theorem of Fontaine and the comparison of Step 3, $E N(M) \subseteq M_R$, and the jumps of $P$ lie in every set that contains the Hodge-Tate jumps of $V$. Since $T$ is good, the jumps of $P$ lie in $U$, so in $[-\eta, H]$. For a $\varphi$-module, the jumps lie in $[-\eta, H]$ if and only if $E^H M \subseteq \varphi^* M$ and $E^\eta \varphi^* M \subseteq M$. This gives the height conditions.

*Step 6: the characters.* A lemma on tame inertia shows that the characters of $\Delta$ at each $\tau$ are among the $\omega^c$ that kill $D_{\mathrm{cris}}$ in the tame type condition. So they lie in $\Sigma$, since $T$ has tame type $\Sigma$.

Steps 1 to 5 give a Breuil-Kisin datum of heights $(\eta, H)$ and a Galois datum, and Step 1 gives the F-crystal condition. So they form a pack, and Steps 5 and 6 show that it is of type $(\Sigma, U)$. $\square$

**Remark 7.14.6 (Formalization).** The steps are lemmas imported from "Statement" files ([ExistsBreuilKisinModuleTameDescentGoodLattice.lean](lean:Development/AbelianVarietyTheory/Proofs/InertiaEigenvalues/ExistsBreuilKisinModuleTameDescentGoodLattice.lean#L21)): `nonempty_crysBKFunctorOL_of_bhattScholze` (Step 1), `breuilKisin_bcris_comparison_frobenius_naturality` and `galois_fixes_crystalline_image_descentDatum` (Step 3), `breuilKisin_tensorAinf_galoisStable_kummerFixed`, `kummerTowerGalois_preserves_breuilKisinModule` and `exists_galoisDescentDatum_and_stable` (Step 4), `PhiMod.jumps_subset_Icc_iff` (Step 5) and `tameInertiaCharacters_subset_tameType` (Step 6). We read their uses and not their proofs, so the descriptions of Steps 3, 4 and 6 follow the names. The comparison lemma also returns a naturality statement that the proof discards (line 29). The bound $H$ enters only through $U \subseteq [-\eta, H]$. We did not unfold the tame Galois group, the characters of a descent datum, or the compatibility of the descent datum with the Galois action. The second name is a one-line wrapper.

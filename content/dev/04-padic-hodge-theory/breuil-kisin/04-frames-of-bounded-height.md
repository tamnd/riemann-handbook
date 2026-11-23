---
title: Frames of bounded height
decls:
  - GlobalTheory.BKLim.exists_frame_sst
  - GlobalTheory.T.exists_breuilKisinFrame_semistable_boundedJumps
status: drafted
drafted_by: writer@claude-opus-5-5
---
## Frames of bounded height

This section proves the main theorem of the chapter on a single lattice. Let $\rho : G_K \to \mathrm{GL}_d(\mathbb{Z}_\ell)$ be continuous with $V = \mathbb{Q}_\ell^d$ semistable, and assume that the Hodge-Tate jumps of $V$ lie between $-N$ and $N$. Then $\rho$ has a de Rham frame of height $N$, and the frame is crystalline when $V$ is crystalline. The point is that the height depends only on the jumps, not on the lattice. This uniformity is what allows [the limit construction](/entry/limit-frame-exists/) of the next section to pass from the layers of a tower of lattices to its limit. The theorem is applied to each layer in the proof of [the theorem on covers](/entry/closed-of-cover/) at the end of this chapter, and it is one of the inputs of [the theorem on the core of the Galois row](/entry/core-all-of/). We keep the notation of the previous sections: a Breuil-Kisin datum for $K$, its disc rings, and a Frobenius period $\tau$.

The proof builds a semistable period datum, applies [the theorem on frames from period data](/entry/semistable-period-frame/), and then lowers the height of the frame to $N$. In the semistable case the period datum comes from [the period matrices over $A_{\mathrm{cris}}$](/entry/sst-periods/). In the crystalline case it comes from a separate construction, with trivial cocycle.

**Definition 3.4.1 (Crystalline period datum).** Let $\rho : G_K \to M_d(\mathbb{Z}_\ell)$ be a map. A *crystalline period datum* for $\rho$ and $\tau$ consists of integers $N, c_1, c_2, c_3 \geq 0$ and matrices $F, F'$, $X, X'$, $W, W'$ as in a [semistable period datum](/entry/semistable-period-frame/), with $FF' = \ell^{c_3}$, $XX' = \ell^{c_2} E^{2N}$, $WW' = \tau^{2N}$ and property 1 of that definition, such that:

1. For every $g \in G_K$ and every action $\Gamma$ of $g$ on $D_A$, $(E\tau)^N \rho(g) \, \Gamma(W X') = g(E\tau)^N \, W X'$.
2. For every prism $B$ over $\mathcal{O}_K$ and every two maps of prisms $f, h$ from the Breuil-Kisin prism $(\mathfrak{S}, (E))$ to $B$, there is $k \geq 0$ such that $f(E)^{2N}$ divides each entry of $\ell^k f(X') h(X)$.

So a crystalline period datum is a semistable period datum with $\kappa = 1$ in property 2, except that the condition on poles is asked after any two maps to a prism, not after the Galois action on $D_A$.

**Lemma 3.4.2 (Crystalline period data exist).** Let $\rho : G_K \to \mathrm{GL}_d(\mathbb{Z}_\ell)$ be a continuous homomorphism such that $V = \mathbb{Q}_\ell^d$ is crystalline. Then there is a crystalline period datum for $\rho$ and $\tau$.

Lean: `GlobalTheory.BKLim.crys_seed`.

**Lemma 3.4.3 (Trivial cocycle).** Let $\rho : G_K \to M_d(\mathbb{Z}_\ell)$ be a map. Every crystalline period datum for $\rho$ and $\tau$ gives a semistable period datum for $\rho$ and $\tau$ with $\kappa(g) = 1$ for all $g \in G_K$.

Lean: `GlobalTheory.T.exists_trivial_cocycle_crystalline_period_data`.

**Lemma 3.4.4 (Period data from $A_{\mathrm{cris}}$).** Let $\rho : G_K \to M_d(\mathbb{Z}_\ell)$ be a map, and let $N, c_1, c_2, c_3, k_0$, $F, F'$, $X, X'$, $Z, Z'$ and $\kappa : G_K \to M_d(A_{\mathrm{cris}})$ satisfy properties 1 to 6 of [the theorem on period matrices](/entry/sst-periods/). Then there is a semistable period datum for $\rho$ and $\tau$.

Lean: `GlobalTheory.T.semistableSeed_of_acris_periods`.

The cocycle of the new datum is not asserted to be related to $\kappa$. In particular this lemma gives no crystalline frame, which is why the crystalline case is treated apart.

**Lemma 3.4.5 (Lowering the height).** Assume that $B_{\mathrm{dR}}^{G_{K'}} = K'$ for every finite extension $K'$ of $\mathbb{Q}_\ell$ in $\Omega$. Let $\rho : G_K \to M_d(\mathbb{Z}_\ell)$ be a map, $N, N_0 \geq 0$, and let $F$ be a de Rham frame of height $N$ for $\rho$. Assume that $\rho$ has a [Hodge basis](/entry/sst-periods/) for $\xi = E$ over $K$ with $|p_i - q| \leq N_0$ for all $i$. Then there is a frame of height $N_0$ for $\rho$ with the same matrix $T$ and the same cocycle $\varepsilon$ as $F$.

Lean: `GlobalTheory.T.exists_breuilKisin_frame_height_of_jumps_le`.

Only the matrices $A$ and $A'$ change: the lemma gives $A_0, A_0' \in M_d(\mathfrak{S})$ with $E^{N_0} \varphi(T) = TA_0$ and $A_0 A_0' = E^{2N_0}$. So the height of a de Rham frame is controlled by the jumps of the representation, whatever height the construction first produced.

**Theorem 3.4.6 (Frames of bounded height).** Let $\tau$ be a Frobenius period and $N \geq 0$. Let $\rho : G_K \to \mathrm{GL}_d(\mathbb{Z}_\ell)$ be a continuous homomorphism such that $V = \mathbb{Q}_\ell^d$ is semistable, $D_{\mathrm{dR}}(V) \subseteq \mathrm{Fil}^{-N}(V)$ and $D_{\mathrm{dR}}(V) \cap \mathrm{Fil}^{N+1}(V) = 0$. Then there is a frame $F$ of height $N$ for $\rho$ that is de Rham, and $F$ is crystalline if $V$ is crystalline.

Lean: `GlobalTheory.BKLim.exists_frame_sst` (also `GlobalTheory.T.exists_breuilKisinFrame_semistable_boundedJumps`, a second name).

The two conditions on $D_{\mathrm{dR}}(V)$ say that the [Hodge-Tate jumps](/entry/sst-periods/) of $V$ at each embedding lie in the interval from $-N$ to $N$: the first says that the filtration of $D_{\mathrm{dR}}(V)$ is everything in degree $-N$, and the second that it is zero in degree $N + 1$.

*Proof.* By [the lemma that semistable representations are de Rham](/entry/sst-periods/), $V$ is de Rham. Since $E$ generates $\ker \theta$, [the lemma on Hodge bases](/entry/sst-periods/) gives a Hodge basis of $\rho$ for $\xi = E$ over $K$, and the hypothesis on $D_{\mathrm{dR}}(V)$ gives $|p_i - q| \leq N$ for all $i$.

Next we find a semistable period datum $s$ for $\rho$ and $\tau$ whose cocycle is trivial when $V$ is crystalline. If $V$ is crystalline, the lemma that crystalline period data exist (which uses that $\rho$ is continuous) gives a crystalline period datum, and the lemma on the trivial cocycle turns it into a semistable period datum with $\kappa = 1$. If $V$ is not crystalline, [the theorem on period matrices](/entry/sst-periods/) gives matrices with properties 1 to 6, and the lemma on period data from $A_{\mathrm{cris}}$ gives $s$; the condition on the cocycle is then empty.

Each $\rho(g)$ is invertible. So [the theorem on frames from period data](/entry/semistable-period-frame/) gives some $N'$ and a de Rham frame $F$ of height $N'$ for $\rho$, which is crystalline if the cocycle of $s$ is trivial, so in particular if $V$ is crystalline. By Fontaine's theorem, $B_{\mathrm{dR}}^{G_{K'}} = K'$ for every finite extension $K'$. So the lemma on lowering the height, applied to $F$ and the Hodge basis, gives a frame $F_0$ of height $N$ with the same $T$ and $\varepsilon$. The de Rham and crystalline conditions depend only on $\varepsilon$, so $F_0$ is de Rham, and it is crystalline when $V$ is. $\square$

**Remark 3.4.7 (Formalization).** Continuity of $\rho$ is used only in the crystalline case, through the crystalline period data, which are built by `GlobalTheory.SeedExists.exists_seed` applied to the standard lattice $\mathbb{Z}_\ell^d$ with its standard basis ([ExistsBreuilKisinFrameSemistableBoundedJumps.lean](lean:Development/AbelianVarietyTheory/Proofs/InertiaEigenvalues/ExistsBreuilKisinFrameSemistableBoundedJumps.lean#L102)). In the other case the clause "crystalline implies the frame is crystalline" is proved by contradiction with the case hypothesis. The crystalline period datum is the structure `Seed`, and a prism over $\mathcal{O}_K$ is an object of `GlobalTheory.Prism.Obj`: a $\delta$-ring $A$ with an invertible ideal $I$, complete for $(\ell) + I$, with $\ell^\infty$-torsion of $A/I$ of bounded exponent, and with a map $\mathcal{O}_K \to A/I$. The period rings in the statement are those of an abstract model (`LocPrime`, `LocAinf`, `LocTied`), and the proof first chooses a concrete core of period rings that fits the model (`MemLoc.FitsEx.exists_fits`); Fontaine's theorem $B_{\mathrm{dR}}^{G_{K'}} = K'$ is a field of that fit. The lemma on period data from $A_{\mathrm{cris}}$ takes a core of period rings but no hypothesis that it fits the model. The four lemmas of the proof and the Hodge basis lemma are not unfolded. The second name has the same type and is proved by applying the theorem.

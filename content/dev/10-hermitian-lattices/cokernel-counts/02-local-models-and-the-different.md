---
title: Local models and the different
decls:
  - Formalism.L2.SG.Pf.localModelS_of
  - Formalism.L2.SG.Pf.localModelS_of_delta
  - Formalism.L2.SG.Pf.localModelS_holds
  - Formalism.L2.SG.Pf.localModelAt_holds
status: drafted
drafted_by: writer@claude-opus-5-5
---
## Local models and the different

The counts of this chapter are products of local counts, one for each finite place. To compare a global count with the product, each local factor must be computed with the right additive character, and the characters at the different places must fit together. This section shows that they do. The key input is the product formula for the module of a local element, applied to the local components of the different of $F$. The main result, the Theorem (Local model at every place), says that the local data of every word pair satisfy the three conditions of a local model. It is used in [Theorem 3.9.4](/entry/theorem-s-leaves-of-carrier-g/), the step that cuts the coefficient of a Hecke operator into its leaves.

Let $E/F$ be a CM extension of number fields, with $[F : \mathbb{Q}] = f$ and so $[E : \mathbb{Q}] = 2f$. For a finite place $p$ of $F$ let $F_p$ be the completion ([places and completions](/learn/number-fields/#places-and-completions)), $\mathcal{O}_p$ its ring of integers and $E_p = E \otimes_F F_p$.

**Definition 8.2.1 (Module of an element).** Let $R$ be a compact open subring of a local field $L$ and $x \in L^\times$. The *module* of $x$ is
$$|x|_R = \frac{[R : R \cap xR]}{[xR : R \cap xR]},$$
the factor by which multiplication by $x$ scales a [Haar measure](/learn/analysis/#haar-measure) on $L$. If $R = \mathcal{O}_L$ and $x = \varpi^k u$ with $u$ a unit, then $|x|_R = q^{-k}$, where $q$ is the order of the residue field.

**Definition 8.2.2 (Agreeing local data).** A family of *local data* is a pair $(\delta, M)$, where $\delta = (\delta_p)$ with $\delta_p \in F_p^\times$, and $M = (M_p)$ is a family of local models: $M_p$ is a choice of a lattice ring, an involution and an additive character $\psi_{0,p}$ of $E_p$, and of a splitting $E_p \cong F_p \times F_p$ when $p$ splits in $E$. The data *agree* with the fixed global datum if at each $p$ the model is admissible, $\delta_p \neq 0$, the ring and the involution of $M_p$ are those of $E_p$, the splitting of $M_p$ is the one of $E_p$ (when $p$ is split), and
$$\psi_{0,p}(y) = \psi_{E,p}\bigl(-y \, \delta_p^{-1}\bigr) \quad (y \in E_p),$$
where $\psi_{E,p}$ is the local component of the fixed standard character of $\mathbb{A}_E / E$.

So $\delta_p$ measures how far the local character $\psi_{0,p}$ is from the standard one. The local character used in the counts has conductor $\mathcal{O}_{E,p}$, while the standard character has conductor the inverse different. So $\delta_p$ is a generator of the local different of $F$, up to a unit. The next theorem records the product of the modules of the $\delta_p$.

**Theorem 8.2.3 (Product of the local differents).** Let $(\delta, M)$ agree with the global datum. Then $|\delta_p|_{\mathcal{O}_{E,p}} = 1$ for almost all $p$, and
$$\prod_p |\delta_p|_{\mathcal{O}_{E,p}} = \bigl(\mathrm{rd}_E^{\,2f}\bigr)^{-1},$$
where $\mathrm{rd}_E = |d_E|^{1/[E:\mathbb{Q}]}$ is the root discriminant of $E$.

Lean: `Formalism.L2.SG.Pf.deltaProd_holds`.

*Proof.* At each $p$ the element $\delta_p$ generates the $p$-part $\mathfrak{d}_{F,p}$ of the different of $F$, because $\psi_{0,p}$ and the standard character have conductors $\mathcal{O}_{E,p}$ and $\mathfrak{d}_{F,p}^{-1}\mathcal{O}_{E,p}$. Since $E_p$ has degree $2$ over $F_p$, the module of $\delta_p$ on $E_p$ is the square of its module on $F_p$, which is $N(\mathfrak{d}_{F,p})^{-2}$. This is $1$ unless $p$ divides the different, so only finitely many factors differ from $1$. The product is $N(\mathfrak{d}_F)^{-2} = |d_F|^{-2}$, because the norm of the different is the absolute value of the discriminant (Neukirch, Chapter III, §2). Finally $\mathrm{rd}_E^{\,2f} = |d_E|$, and $|d_E| = d_F^{\,2}$ since $E/F$ is unramified at all finite places. $\square$

From this the product formula gives the module of the rescaled local coordinates.

**Lemma 8.2.4 (Modules of rescaled coordinates).** Let $(\delta, M)$ agree with the global datum. For integers $\nu, s \geq 0$ and $t \in E^\times$, let $t_p \in E_p$ be the local coordinate of $t$ at $p$ in level $(\nu, s)$, rescaled by $\delta_p^{-\nu}$ and by fixed local parameters. Then $|t_p| = 1$ for almost all $p$, and $\prod_p |t_p| = N_{\nu}(t)^{-1}$ for an explicit global factor $N_\nu(t)$ built from $|N_{E/\mathbb{Q}}(t)|$ and $\mathrm{rd}_E$.

Lean: `Formalism.L2.SG.Pf.modNorm_of` (also `Formalism.L2.SG.Pf.ModNorm`, the statement).

*Proof.* By the product formula ([adeles and ideles](/learn/number-fields/#adeles-and-ideles)), the product of the modules $|t|_v$ over all places of $E$ is $1$, so the product over the finite places is $|N_{E/\mathbb{Q}}(t)|^{-1}$. The factor $\delta_p^{-\nu}$ contributes the $\nu$-th power of the inverse of the product in the Theorem (Product of the local differents). The fixed local parameters contribute a fixed global constant. $\square$

**Definition 8.2.5 (Local model).** Fix the global datum. For each choice of the auxiliary data (two weights, a Hida setting $S$ and agreeing local data $(\delta, M)$) and each pair of words $u, u'$ that are compatible in $S$, there is a local datum $d(S, \delta, M, u, u')$: a family of kernels $K_i$ for $i \leq r + 1$, built from the local kernels $K_p$ at the places $p$ of $F$, with the normalizing factors $a(x)$ and $d_p(x)$. We say that a condition $P$ holds *at every place* if $P(d(S, \delta, M, u, u'))$ holds for all such choices. The three conditions are as follows.

1. *Kernel form.* For each level $i$ and points $x, y$,
$$K_i(x, y) = a(x) a(y) \prod_p [\mathrm{cl}_p x = \mathrm{cl}_p y] \, d_p(x) \, \overline{d_p(y)} \, K_p(\eta_p x, \eta_p y),$$
where $\mathrm{cl}_p$ is the local class map and $\eta_p$ the local coordinate.
2. *Slices.* For $1 \leq s \leq i \leq r + 1$ and each finite set $Y$ of points at level $i - s$, there are local systems $S_p$ (of top, pullback or outer kind) such that the system at $(i, s)$ is the scaled product of the $S_p$, with lower lattice the intersection of the local lattices and upper lattice containing it.
3. *Top orthogonality.* At level $r + 1$, $K_{r+1}(x, y) = 0$ when $x$ and $y$ are joins over different classes $t \neq t'$.

A datum that satisfies all three is a *local model*.

**Theorem 8.2.6 (Slices hold at every place).** Assume the conclusion of the Lemma (Modules of rescaled coordinates). Then the slice condition holds at every place.

Lean: `Formalism.L2.SG.Pf.localModelS_of`.

*Proof.* Fix the choices and the words. In the top case $i = r + 1$, $s = 1$, the system is the top system and the local systems $S_p$ are the top local systems. The scale is the product of the modules of the local coordinates, and the Lemma (Modules of rescaled coordinates) gives its value as a global norm factor. In the other cases the system at $(i, s)$ is pulled back from level $i - s$ along $Y$, and the local systems are pullbacks at the places in the support and outer systems elsewhere. The lattice conditions hold place by place, because a lattice in a product of local spaces is the intersection of its local components. The finiteness of the supports in the Lemma makes the product a finite product. $\square$

**Corollary 8.2.7 (Slices from the different).** Assume the conclusion of the Theorem (Product of the local differents). Then the slice condition holds at every place.

Lean: `Formalism.L2.SG.Pf.localModelS_of_delta`.

*Proof.* This is the [Theorem (Slices hold at every place)](/entry/local-model-s-of/) applied to the Lemma (Modules of rescaled coordinates), which follows from the product of the local differents. $\square$

**Corollary 8.2.8 (Slices).** The slice condition holds at every place.

Lean: `Formalism.L2.SG.Pf.localModelS_holds`.

*Proof.* This is the [Corollary (Slices from the different)](/entry/local-model-s-of-delta/) applied to the Theorem (Product of the local differents). $\square$

**Theorem 8.2.9 (Local model at every place).** For every choice of weights, Hida setting, agreeing local data and compatible words $u, u'$, the local datum $d(S, \delta, M, u, u')$ is a local model.

Lean: `Formalism.L2.SG.Pf.localModelAt_holds`.

*Proof.* The kernel form holds at every place by the construction of the kernels as products of local kernels. The slice condition holds by the [Corollary (Slices)](/entry/local-model-s-holds/). Top orthogonality holds at every place because the top kernel has the factor $[\mathrm{cl}_p x = \mathrm{cl}_p y]$ at each $p$, and joins over different classes $t \neq t'$ differ in their class at some place. The three conditions together are the definition of a local model. $\square$

**Remark 8.2.10 (Formalization).** The proof of the corollary from the different ([LocModelKSN.lean](lean:Formalism/LocalToGlobal/SiegelLatticeTheory/CokernelGLCounts/RankPointCounts/LocModelKSN.lean#L319)) is a chain of `first | exact …` tries over several names (lines 320 to 324), so the proof term that is used is the one that elaborates first, not one that is written down. We did not unfold the rescaled coordinate `tMod`, the twist, the local parameters or the norm factor `nrm`, so the Lemma (Modules of rescaled coordinates) is stated only in outline. The slice proof (LocModelKS.lean:1680) is long. We give its split into the top case and the other cases, and we did not check every case. The kernel form and top orthogonality are the separate results `localModelK_holds` and `localModelT_holds`, which we did not open in detail.

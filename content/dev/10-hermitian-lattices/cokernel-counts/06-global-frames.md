---
title: Global frames and local indices
decls:
  - Formalism.L2.SG.Pf.FrameGlobalPatching.FStar.lprPart_holds
  - Formalism.L2.SG.Pf.FrameGlobalPatching.FStar.fStarC_of_leaves'
  - Formalism.L2.SG.Pf.FrameGlobalPatching.FStar.fStarC_of_beta
  - Formalism.L2.SG.Pf.FrameGlobalPatching.FStar.fStarC_of_int
  - Formalism.L2.SG.Pf.CountAt.countAt_holds
  - Formalism.L2.SG.Pf.FrameGlobalPatching.FStar.cutLeavesDeep_of_betaInt
status: drafted
drafted_by: writer@claude-opus-5-5
---
## Global frames and local indices

The local cut of the [previous section](/entry/cut-at-of-deep/) needs three global inputs. The first is a bijection between partner classes of a term and global lattices with given local components: this is a local-to-global principle for lattices with a frame. The second is that the local weight of a term is a finite index of a stabilizer image. The third is the approximation of stabilizers. This section proves the first two and assembles the three. The main result, the Theorem (Deep cut from the integral beta condition), is used in the [Theorem 5.9.2](/entry/cut-leaves-deep-outright/) that proves the deep cut outright.

Fix the global datum, agreeing local data $(\delta, M)$, words $u, u'$ with the congruence and prime conditions, and row representatives $(F_0, \mathcal{W})$ as in the [previous section](/entry/cut-at-of-leaves/). A *global term* $\gamma$ has a lattice $\Lambda_\gamma$ and two frames, and for each finite place $p$ its local lattice $\Lambda_{\gamma, p}$. A *partner* of $\gamma$ with second frame $F'$ is a global lattice $\Lambda'$ such that $(\Lambda', F_0, F')$ is a term with the same local data as $\gamma$. Let $N_0(F_0, \Lambda_\gamma)$ be the group of unipotent isometries that fix $F_0$ and preserve $\Lambda_\gamma$.

**Definition 8.6.1 (Global frame bijection).** We say that the *global frame bijection* holds at $(u, u', F_0, \mathcal{W})$ if, for every global term $\gamma$ and second frame $F'$, the orbits of $N_0(F_0, \Lambda_\gamma)$ on the partners of $\gamma$ are in bijection with the global lattices whose local components are the prescribed local partners at each $p$.

**Definition 8.6.2 (Local partner transport).** The *local partner transport* holds if, at every finite place $p$, for every local isomorphism $\psi$ from the second frame of $\gamma$ to $F'$ that identifies the two frames, $\psi$ maps the set of local lattices of $\gamma$ at $p$ onto the set of local lattices of $(\Lambda_{\gamma, p}, F')$. In the split case $\psi$ also maps the graph $\iota$ of the local splitting of $\gamma$ to that of $(\Lambda_{\gamma,p}, F')$.

**Theorem 8.6.3 (Local partner transport).** The local partner transport holds.

Lean: `Formalism.L2.SG.Pf.FrameGlobalPatching.FStar.lprPart_holds`.

*Proof.* It follows from the iota step, which treats the graph $\iota = \{(x', x) : x, x' \in \Lambda, \ x - x' \in q \Lambda\}$ of the split case: an isomorphism that identifies the frames maps this graph for $\gamma$ to the graph for $(\Lambda_{\gamma,p}, F')$. $\square$

**Theorem 8.6.4 (Global frame bijection from the local transport).** Assume the standing context conditions on $(u, u', F_0, \mathcal{W})$, the local partner transport, and the rational and integral beta conditions (defined below). Then the global frame bijection holds.

Lean: `Formalism.L2.SG.Pf.FrameGlobalPatching.FStar.fStarC_of_leaves'`.

*Proof.* The bijection is built from four facts. Existence: a starting global partner exists under the context conditions. Forward map: a global partner gives local partners by localization, and the local partner transport shows that they are of the prescribed kind. Backward map: given local partners, the rational and integral beta conditions give an isometry $v$ that moves the starting partner to a global lattice with these components. Uniqueness: two global partners with the same local components lie in one orbit of $N_0(F_0, \Lambda_\gamma)$. The forward and backward maps are inverse on orbits. $\square$

**Corollary 8.6.5 (Global frame bijection from the beta conditions).** Assume the standing context conditions and the rational and integral beta conditions. Then the global frame bijection holds.

Lean: `Formalism.L2.SG.Pf.FrameGlobalPatching.FStar.fStarC_of_beta`.

*Proof.* This is the [Theorem (Global frame bijection from the local transport)](/entry/f-star-c-of-leaves-prime/) applied to the [Theorem (Local partner transport)](/entry/lpr-part-holds/). $\square$

**Definition 8.6.6 (Integral beta condition).** The *integral beta condition* holds at $(F_0, \mathcal{W})$ if, for every pair of global terms in the standing setting and every isometry $\beta_0$ that sends the frame of $\gamma$ to the frame of a second term $F'_2$ (with the two compatibility conditions on the frames), there is an isometry $v$ that fixes the frame of $F'_2$, satisfies $v y - y \in X$ for $y \perp X$, where $X$ is the frame space, maps $\beta_0(\Lambda_\gamma)$ onto $\Lambda_2$, and is compatible with the splitting graphs. The *rational beta condition* is the same statement with $v$ only required to be rational.

**Corollary 8.6.7 (Global frame bijection from the integral condition).** Assume the standing context conditions and the integral beta condition. Then the global frame bijection holds.

Lean: `Formalism.L2.SG.Pf.FrameGlobalPatching.FStar.fStarC_of_int`.

*Proof.* This is the [Corollary (Global frame bijection from the beta conditions)](/entry/f-star-c-of-beta/), applied with the rational beta condition, which holds for all data. $\square$

Now the local weights. For a place $p$ and a term, let $P$ be the parabolic subgroup that fixes the frame, $\mathrm{Stab}_P$ the stabilizer in $P(F_p)$ of the local data, $K_p$ the compact open subgroup of the level ([compact open subgroups](/learn/groups/#adelic-points-and-compact-open-subgroups)), and $X_p$ the local frame space.

**Definition 8.6.8 (Index form of a local weight).** A number $v \geq 0$ is in *index form* at $p$ if there are a subgroup $N$, a retraction $\pi \colon \mathrm{Stab}_P \to N$ with $K_p \cap \mathrm{Stab}(X_p) \leq N$, an element $g_0 \in N$, and a subgroup $A_g$ that contains the image $\pi(K_p \cap \mathrm{Stab}_P)$ with finite nonzero relative index, such that $v = [A_g : \pi(K_p \cap \mathrm{Stab}_P)]$.

**Theorem 8.6.9 (Local weights are indices).** Under the standing hypotheses, at every finite place $p$ the local weight of a term (the local lattice weight, with its sign) is in index form.

Lean: `Formalism.L2.SG.Pf.CountAt.countAt_holds`.

*Proof.* Represent $w$ by a local matrix $a$, and take the block retraction $\pi$ for $a$, with kernel in the level subgroup. An element $g$ of the unipotent group moves $a$ to the matrix $Z_0$, which is the modified Gram matrix of the frames, with its sign, plus the shift of $w$. The local weight is finite and equals the number of orbits of the level subgroup on the cells of the orbit of $Z_0$. These cells correspond to the cosets of the image of the stabilizer under $\pi$, so the weight is the index. The index is nonzero because the cell of the identity is one of the cosets, and their number is finite. $\square$

**Theorem 8.6.10 (Deep cut from the integral beta condition).** Assume the integral beta condition for all base flags and row sets. Then the deep cut holds: for all $(\delta, M)$, $(u, u')$ and row representatives $(F_0, \mathcal{W})$, the local index steps hold, the stabilizers have global approximation, and the global frame bijection holds.

Lean: `Formalism.L2.SG.Pf.FrameGlobalPatching.FStar.cutLeavesDeep_of_betaInt`.

*Proof.* The local index steps are the [Theorem (Local weights are indices)](/entry/count-at-holds/) together with the unimodularity of the local lattices at each place. The approximation of stabilizers is a separate result on global tuples. The context conditions hold in the standing setting, and the global frame bijection is the [Corollary (Global frame bijection from the integral condition)](/entry/f-star-c-of-int/). $\square$

**Remark 8.6.11 (Formalization).** The last theorem asks for the integral beta condition for all base flags and all row sets ([FStarCut.lean](lean:Formalism/LocalToGlobal/SiegelLatticeTheory/CokernelGLCounts/RankPointCounts/FStarCut.lean#L16)), but uses it only at the given ones. The two corollaries from the integral and the beta conditions could be one step: the second only inserts the rational beta condition. The file of the integral corollary is named after a different statement (FrGlobPOfInt.lean:18, while the statement with that name is in PartnerCountP.lean:23). The bijection theorem from the local transport has a primed name and no unprimed version. We read the statements of the existence, forward, backward and uniqueness parts and of the iota step, but did not check their proofs; the proofs above give their roles. In the index form, $v$ is the relative index of subgroups, which is $0$ when the index is infinite; the condition that it is nonzero excludes this.

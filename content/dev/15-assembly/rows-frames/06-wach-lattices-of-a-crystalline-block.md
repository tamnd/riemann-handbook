---
title: Wach lattices of a crystalline block
decls:
  - GlobalTheory.WachPlace.latAt_of_frame
  - GlobalTheory.WachPlace.exists_positions
  - GlobalTheory.WachPlace.exists_positions_global
  - GlobalTheory.T.wachLattices_rankOne_models_reducedFiltration
  - GlobalTheory.WachPlace.wach_lattices
  - GlobalTheory.T.crystalline_block_lattices_over_power_series_ring
  - GlobalTheory.WachBlock.wach_inputs
  - GlobalTheory.T.crystallineLatticeLink_of_blockData
  - GlobalTheory.ExpLink.latticeLink_of_blockFor
status: drafted
drafted_by: writer@claude-opus-5-5
---
## Wach lattices of a crystalline block

This section turns a crystalline block at a prime $\ell$ into a lattice link: labels on the embeddings of a CM field, carried by lattices of Wach type over a power series ring. A *crystalline block* is a crystalline representation of $G_E$ whose characteristic polynomials are congruent to those of a smaller representation times a product of crystalline characters. The lattice link is used by [the model statement for a small frame](/entry/model-st-of-small-frame-gal/), in the surjectivity branch of [the unitary hypotheses](/proof/unitary-hypotheses/). The only input from the literature is the existence of crystalline lattices of Bhatt and Scholze, in the form of a local theory of Wach modules with frames and comparison maps. We build the lattices one Frobenius orbit of embeddings at a time, glue the orbits, and then read off the labels.

We use [crystalline representations](/learn/padic-hodge/#crystalline-and-semistable-representations) and [Wach and Breuil-Kisin lattices](/learn/padic-hodge/#lattices-wach-breuil-kisin-and-prismatic-f-crystals) of Volume 1.

Let $E$ be a number field and $\ell \neq 2$ a prime with $\ell \nmid \mathrm{disc}(E)$. Let $\Phi$ be the set of embeddings $E \to \overline{\mathbb{Q}}_\ell$. A *Frobenius permutation* is a permutation $\sigma$ of $\Phi$ with $|\sigma\tau(x) - \tau(x)^\ell| < 1$ for all $x \in \mathcal{O}_E$ and $\tau \in \Phi$. Let $L$ be a finite extension of $\mathbb{Q}_\ell$ that contains the $\ell$-th roots of unity and all $\tau(E)$, with ring of integers $\mathcal{O}_L$, uniformizer $\varpi$ and residue field $F$. Fix a unit $u = 1 + \ell c$ of $\mathbb{Z}_\ell$ with $c$ a unit, a power series $u_n$ attached to $u$, a primitive $\ell$-th root of unity $\zeta$, and for $0 < a < \ell$ the maps $j_a$ of $\mathcal{O}_L[[X]]$ that send $X$ to $\zeta^a \exp(X) - 1$.

A *lattice datum* of rank $n$ gives, for each $\tau \in \Phi$, three $n \times n$ matrices: $P_\tau$ over $\mathcal{O}_L[[X]]$ for the Frobenius, $D_\tau$ over $\mathcal{O}_L[[X]]$ for the action of a generator $\gamma$ of the cyclotomic group, and a constant matrix $\Theta_\tau$. Fix a period ring that contains $\mathcal{O}_L[[X]]$ through a map that sends $X$ to an element $\pi_0$, and an element $q$ of it. The datum is *Wach of weights $J$ and height $h$* at $\tau$ if:

1. after the substitution $X \mapsto \pi_0$ there is a matrix $Q$ with $P_\tau Q = q^h \cdot 1$;
2. $X - \ell$ divides each entry of $D_\tau - \Theta_\tau$;
3. for $0 < a < \ell$, after $j_a$ we have $P_\tau = G \, \mathrm{diag}\big(X^{J(\tau, 0)}, \dots, X^{J(\tau, n-1)}\big) H$ with invertible $G$ and $H$, compatible with the action of $\gamma$.

These are the matrices of a Wach module in a basis, with weights $J(\tau, \cdot)$; see Berger, Compositio Math. 140 (2004). We call the datum Wach at $\tau$, and *Wach* if it is Wach at every $\tau$.

**Lemma 7.6.1 (A frame gives a Wach datum at one place).** Let $K$ be unramified over $\mathbb{Q}_\ell$ and let $r$ be a crystalline representation of $G_K$ on a lattice. Let $b$ be a frame of the Wach module of the lattice of $r$: a basis in which the Frobenius has a matrix with cofactor dividing a power of $q$, and the action of $\gamma$ is congruent to its constant term. Let the cyclotomic character send $\gamma$ to $u$. Then the matrices of $b$ form a lattice datum that is Wach at the slot $i$ of $b$.

Lean: `GlobalTheory.WachPlace.latAt_of_frame`.

*Proof.* Condition 1 is the cofactor property of the frame: the Frobenius matrix at $\pi_0$ divides $q^h$. Condition 2 is the congruence of $\gamma$ with its constant term, at slot $i$. For condition 3, fix $0 < a < \ell$. Since $\ell$ is prime, $\zeta^a$ is again a primitive $\ell$-th root of unity. The factor theorem for the Frobenius matrix of a frame at a primitive root gives the elementary divisors after $j_a$. $\square$

A *matrix form of a stable chain* for $r$ and characters $\psi_s$, $s < t$, is a chain of lattices
$$\varpi \mathcal{O}_L^n = M_0 \subseteq M_1 \subseteq \dots \subseteq M_R = \mathcal{O}_L^n$$
stable under $r$, given by matrices, with $t$ distinct steps $r_s$ where $M_{r_s + 1} = M_{r_s} + \mathcal{O}_L x_s$ and $r(g) x_s \equiv \psi_s(g) x_s$ modulo $M_{r_s}$. At each other step the reduced rank does not grow. A *chain of slots* at $(\tau, \sigma\tau)$ is a tuple $y_\tau$ of matrices over $F[[X]]$ that intertwine the reduced Frobenius and $\gamma$ of $N$ and of the rank one data $N_{\psi,s}$, with the reduced ranks of the chain over $F((X))$, and that satisfy the line relations of the chain.

**Lemma 7.6.2 (Positions on one orbit).** Let $K$ be unramified over $\mathbb{Q}_\ell$ of degree $f$, with the embeddings of one Frobenius orbit indexed by $\mathbb{Z}/f$. Let $r$ and $\psi_s$ be crystalline representations of $G_K$ with weights in $[0, h]$, and let $x$ be a matrix form of a stable chain. Assume the local Wach theory. Then there are lattice data $N$ of rank $n$ and $N_{\psi,s}$ of rank one, and slots $y_i$ for $i \in \mathbb{Z}/f$, such that $N$ and each $N_{\psi,s}$ are Wach at each $i$, and $y_i$ and $y_{i-1}$ form a chain of slots.

Lean: `GlobalTheory.WachPlace.exists_positions`.

*Proof.* The local Wach theory gives a frame of the Wach module for $r$, for the lattice at each step of the chain, for each $\psi_s$, and for the extensions at the steps $r_s$. It gives each frame by an invariant basis of the Wach module, which exists since the jumps are nonnegative. The last lemma makes each of these frames a Wach datum at each slot. The maps of the chain are maps of lattices, so by the local theory they give maps of Wach modules. Their matrices in the frames are over $\mathcal{O}_L[[X]]$. Reduce them modulo $\varpi$ to get the slots $y_i$. The matrix of a composite is the product of the matrices, so the reduced matrices intertwine the reduced Frobenius and $\gamma$. A map of rank zero has matrix zero, which gives the line relations of the chain. $\square$

**Theorem 7.6.3 (Global positions).** Let $\sigma$ be a Frobenius permutation, let $r$ be crystalline of rank $n$ with weights $J(\tau, \cdot) \subseteq [0, h]$, let $\psi_s$, $s < t$, be crystalline characters with weights $w_s(\tau) \in [0, h]$, and let $x$ be a matrix form of a stable chain. Assume the existence of crystalline lattices of Bhatt and Scholze. Then there are lattice data $N$ and $N_{\psi,s}$, Wach with weights $J$ and $w_s$, and slots $y_\tau$ for $\tau \in \Phi$ such that $(y_\tau, y_{\sigma\tau})$ is a chain of slots for every $\tau$.

Lean: `GlobalTheory.WachPlace.exists_positions_global`.

*Proof.* The published input gives the [local Wach theory with its ties](/entry/exists-hw-fon-cmp-ties/). Fix $\tau_0 \in \Phi$. There is an unramified extension $K$ of $\mathbb{Q}_\ell$ of degree $f$, a map $G_K \to G_E$, and an injection $\kappa : \mathbb{Z}/f \to \Phi$ with $\tau_0$ in its image and $\kappa(j - 1) = \sigma(\kappa(j))$. The restrictions of $r$ and $\psi_s$ to $G_K$ are crystalline with the same weights. The last lemma gives data on $\mathbb{Z}/f$ with the chain relation along $j \mapsto j - 1$.

Now we glue. The following holds for any permutation $\sigma$ of a finite set $\Phi$: if for each $\tau_0$ there are an injection into $\Phi$ from a set with a permutation, compatible with $\sigma$ and with $\tau_0$ in its image, and data on that set that satisfy a relation along its permutation, then there are data on all of $\Phi$ that satisfy the relation along $\sigma$. Apply this to the orbits. Being Wach at each $\tau$ is the same as being Wach. $\square$

An *integral block* of rank $n$ with $t$ lines and weights $J$, $\mathrm{bot}$ is a crystalline $r : G_E \to \mathrm{GL}_n(\mathcal{O}_L)$ with weights $J$, crystalline characters $\psi_s$ of weight $\mathrm{bot} + s$ for $s < t$, and an $r$-stable chain as above. A *reduced filtration* for lattice data $N$ and $N_{\psi,s}$ is, for each $\tau$, a flag of $F((X))^n$ from $0$ to the whole space, stable under the reduced Frobenius and $\gamma$ of $N$, with $t$ steps that each add a line on which these act through $N_{\psi,s}$ up to a power of $X$.

**Theorem 7.6.4 (Wach lattices of an integral block).** Let $\sigma$ be a Frobenius permutation, assume the existence of crystalline lattices of Bhatt and Scholze, and let an integral block with weights in $[0, h]$ be given. Then there are a complete domain $\mathcal{O}'$ over $\mathbb{Z}_\ell$ with a residue field $F$, the elements $u$, $c$, $u_n$, $\zeta$ and maps $j_a$ as above, and lattice data $N$ and $N_{\psi,s}$, Wach with weights $J$ and $\mathrm{bot} + s$, whose reductions have a reduced filtration.

Lean: `GlobalTheory.T.wachLattices_rankOne_models_reducedFiltration` (also `GlobalTheory.WachPlace.wach_lattices`).

*Proof.* The ring $\mathcal{O}_L$ is a complete discrete valuation ring with residue characteristic $\ell$; take $\mathcal{O}' = \mathcal{O}_L$. The stable chain has a matrix form, with a jump of one in the reduced rank at each $r_s$. Choose $u$, $c$, $\zeta$ and the $j_a$ from the cyclotomic exponential expansions, and $u_n$ from the unit series. The theorem on global positions gives $N$, $N_{\psi,s}$ and a chain of slots. A chain of slots with one line at each $r_s$ is a reduced filtration. $\square$

A *block pair* is a crystalline $r : G_E \to \mathrm{GL}_n(\overline{\mathbb{Q}}_\ell)$ with weights $J$, a continuous $\rho : G_E \to \mathrm{GL}_a$ with $a + t = n$, and crystalline characters $\chi_s$ of weight $\mathrm{bot} + s$, such that each coefficient of
$$\mathrm{charpoly}\, r(g) - \mathrm{charpoly}\, \rho(g) \prod_{s < t} (X - \chi_s(g))$$
has norm less than $1$ for all $g$. The *Wach inputs* at height $h$ are lattice data $N$ and $N_{\psi,s}$, Wach with weights $J$ and $\mathrm{bot} + s$, with base changes $g_\tau$ over $F[[X]]$, a block index, positions $\mathrm{pos}(s)$, units $w_{\tau,s}$ and exponents $\kappa$, such that after the base change the reduced Frobenius and $\gamma$ of $N$ are block triangular and their diagonal entries at $\mathrm{pos}(s)$ are those of $N_{\psi,s}$ times $w_{\tau,s}$ and $X^{\kappa}$.

**Theorem 7.6.5 (Wach inputs of a block pair).** Let $\sigma$ be a Frobenius permutation and assume the existence of crystalline lattices of Bhatt and Scholze. Let the weights $J$ and $\mathrm{bot} + s$ lie in $[0, h]$. Then each block pair gives Wach inputs at height $h$.

Lean: `GlobalTheory.T.crystalline_block_lattices_over_power_series_ring` (also `GlobalTheory.WachBlock.wach_inputs`).

*Proof.* A block pair gives an integral block over the integers of a finite extension: a stable lattice of $r$ and the chain of the reduction of $r$ with the lines of the $\chi_s$. The last theorem gives the Wach data and a reduced filtration. A reduced filtration of étale $\varphi$-modules over $F((X))$ has adapted bases in which the reduced Frobenius and $\gamma$ are block triangular, with the lines at positions $\mathrm{pos}(s)$; this gives $g_\tau$, the block index, $\mathrm{pos}$, $w$ and $\kappa$. $\square$

Now let $E$ be CM with complex conjugation $c$. A *half* is an injection $\mathrm{inc} : \iota \to \Phi$ such that each embedding is $\mathrm{inc}\,\tau$ or $\overline{\mathrm{inc}\,\tau}$ and never both. For weights $W$ of rank $N$ with highest weights $\lambda_\tau$ and height $h_0$ put
$$U_W(\tau, a) = \lambda_\tau(a) + N - 1 - a.$$
A family $\mu$ is *linked* to $\lambda$ at $\ell$ if each $\mu_\tau$ is decreasing, lies between $\lambda_\tau(N-1)$ and $\lambda_\tau(0)$, has the same sum as $\lambda_\tau$, and
$$\prod_a \big(X + \lambda_\tau(a) - a\big) = \prod_a \big(X + \mu_\tau(a) - a\big) \quad \text{in } \mathbb{F}_\ell[X].$$
A *block for* $\mu$ is a block pair with weights $U_\mu$ on $\mathrm{inc}\,\tau$ and $h_0 - U_\mu$ in reverse order on $\overline{\mathrm{inc}\,\tau}$, with $\mathrm{bot}$ given by $W$, up to a global swap by $c$. A *lattice link* at $\tau$ is a permutation of a finite set, labels on it and Wach inputs at height $h_0$, with labels that are symmetric under $c$, linked, carried by the weights and equal to $U_W$ on $\iota$, and with the permutation sending $\mathrm{inc}\,\tau$ to $\mathrm{inc}(\mathrm{fr}\,\tau)$ or its conjugate as a sign $\mathrm{cj}\,\tau$ says.

**Theorem 7.6.6 (Lattice link of a block).** Let $E$ be CM, $\ell \neq 2$, $\ell \nmid \mathrm{disc}(E)$, $\mathrm{inc}$ a half, and assume the existence of crystalline lattices of Bhatt and Scholze. There are maps $\mathrm{fr} : \iota \to \iota$ and $\mathrm{cj} : \iota \to \{0, 1\}$ with this property. Let parameters $P$ and weights $W$ satisfy their hypotheses, with all $U_W(\tau, a) \in [0, h_0]$. Let $\mu$ be linked to $\lambda$ at $\ell$ and let a block for $\mu$ exist. Then a lattice link holds at every $\tau \in \iota$, with the Frobenius data $\mathrm{fr}$, $\mathrm{cj}$ and the values of $\mu_\tau$.

Lean: `GlobalTheory.T.crystallineLatticeLink_of_blockData` (also `GlobalTheory.ExpLink.latticeLink_of_blockFor`).

*Proof.* Since $\ell \nmid \mathrm{disc}(E)$, $\ell$ is unramified in $E$, and there is a Frobenius permutation $\sigma$ of $\Phi$ that commutes with $c$. Write $\sigma(\mathrm{inc}\,\tau)$ as $\mathrm{inc}\,\tau'$ or $\overline{\mathrm{inc}\,\tau'}$, put $\mathrm{fr}\,\tau = \tau'$, and let $\mathrm{cj}\,\tau = 1$ in the second case. The block for $\mu$ gives $J$, $\mathrm{bot}$ and a block pair. The bounds on $U_W$ and the linkage give $0 \leq J \leq h_0$ and $0 \leq \mathrm{bot} + s \leq h_0$. The last theorem gives the Wach inputs. Take the set $\Phi$, the permutation $\sigma$ and the labels $U_W$ and $U_\mu$ on $\mathrm{inc}\,\iota$, and $h_0$ minus the reversed labels on the conjugates. These labels are symmetric under $c$ by construction, linked by the hypothesis on $\mu$, and carried by $J$ by the choice of the block. $\square$

**Remark 7.6.7 (Formalization).** The published input is `BhattScholzeCrystallineLattices`, used only once, through `HWL.exists_hw_fon_cmp_ties` in the theorem on global positions; all other steps pass it on. The lattice datum is `Lat` with the conditions `LatAt` and `LatN` in [RankOfMulEqOne.lean](lean:Development/AbelianVarietyTheory/Proofs/DivisorProofs/RankOfMulEqOne.lean#L124), and the Wach inputs are `NInputs` in [LemmaWFromLattice.lean](lean:Formalism/PieriBlockIdeals/LemmaWFromLattice.lean#L216). The lemma on frames is at [ExistsSlotsGlobal.lean](lean:Development/AbelianVarietyTheory/Proofs/DivisorProofs/ExistsSlotsGlobal.lean#L53); the lemma on one orbit is at line 124 of that file, with frames from `exists_frame` (line 44), map matrices from `exists_mapMat` (line 79) and `mapMat_mul` (line 103), and the zero map from `eq_zero_of_lrank` (line 24). The gluing lemma is `glue_orbits` at line 207. The theorem on global positions does not use that $E$ is CM. The conclusion of the theorem on Wach lattices does not name $r$, $\psi$ or the chain; for $t = 0$ it holds with the flag $0 \subseteq F((X))^n$, so the link to $r$ lives only in the proof. In the theorem on lattice links, $\mathrm{fr}$ and $\mathrm{cj}$ are functions of an extra argument in $\mathbb{N}$ that they ignore ([CrystallineLatticeLinkOfBlockData.lean](lean:Development/AbelianVarietyTheory/Proofs/DivisorProofs/CrystallineLatticeLinkOfBlockData.lean#L60)), and they do not depend on $P$, $W$ or $\mu$. The three statement files of this section prove each second name by a tactic of the form `first | exact ...` that tries three ways to apply the same theorem, and the file of the lattice link sets `maxHeartbeats` to 1000000 for that one line. We did not unfold the conditions `CrysWith`, `IsCrysAt` and `IsJumpsAt`; "crystalline with weights" above names them.

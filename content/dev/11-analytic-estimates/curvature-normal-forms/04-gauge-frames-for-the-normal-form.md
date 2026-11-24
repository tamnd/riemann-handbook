---
title: Gauge frames for the normal form
decls:
  - Formalism.FourierDecayAlt.P.CutMP.Gauge.GC.genTransfer_of_rotK
  - Formalism.FourierDecayAlt.P.CutMP.Gauge.GC.gauge_locality_holds
  - Formalism.FourierDecayAlt.P.CutMP.Gauge.GC.gTCRef_of_rotK
  - Formalism.FourierDecayAlt.P.CutMP.Gauge.GC.gTConn_of_rotK
  - Formalism.FourierDecayAlt.P.CutMP.Gauge.GC.gTSS_of_adj_radT
  - Formalism.FourierDecayAlt.P.CutMP.Gauge.GC.gTSS_of_adj
  - Formalism.FourierDecayAlt.P.CutMP.Gauge.GC.second_shift_gauge_holds
  - Formalism.FourierDecayAlt.P.CutMP.Gauge.GC.SSPh.second_shift_phase_holds
status: drafted
drafted_by: writer@claude-opus-5-5
---
## Gauge frames for the normal form

This section compares the actual operators of a place with the model operators of the first section. It proves that, under one hypothesis on a rotation generator, every place has an orthonormal frame of its fibres under which the generators of the actual level, the type projections and the raising operators go to the model operators of the same name. The frame is found in stages: a frame that carries the type projections, a phase change that fixes the covariant derivatives, and a constant phase change that fixes the raising operators. The last stage uses [the extra relations from a start](/entry/shift-extra/). The result gives the gauge core of a place and then the model place, which the step [nonempty hypotheses](/step/nonempty-hyps/) uses.

### Frames and the transfer

Fix a parameter $P$ with $k \ge 2$ and a place of $P$: two points $z$, $z'$, representations on finite dimensional Hilbert spaces $W_p$ and $W_q$, and the space $\mathcal{R}$ of radial functions $\Phi(c, g)$ with values in $\mathrm{Hom}(W_q, W_p)$. Let $\Omega = \{\zeta : |\zeta|^2 > T_2\}$ and $G(\zeta) = |\zeta|^2 - T_2$. A *section* $\mu$ maps $\mathbb{C}$ to $(k+1) \times (k+1)$ matrices, and each $\zeta \in \Omega$ has a *fibre* $F_\zeta \subset \mathrm{Hom}(W_q, W_p)$, the values allowed at $\mu(\zeta)$. The space $\mathrm{Hom}(W_q, W_p)$ has the Hilbert-Schmidt inner product, linear in the second slot. The section is *constant* if the stabilizer of $\mu(\zeta)$ is the same for all $\zeta \in \Omega$.

**Definition 1.4.1 (Frame).** A *frame* is a family $e = (e_\rho)$ of smooth maps $\Omega \to \mathrm{Hom}(W_q, W_p)$, indexed by the types $\rho$ of $P$, such that for every $\zeta \in \Omega$ the elements $e_\rho(\zeta)$ lie in $F_\zeta$, are orthonormal, and span $F_\zeta$: every $X \in F_\zeta$ equals $\sum_\rho \langle e_\rho(\zeta), X \rangle\, e_\rho(\zeta)$.

**Definition 1.4.2 (Transfer).** The *transfer* of $\Phi \in \mathcal{R}$ under a frame $e$ is

$$\mathrm{tr}_e \Phi(\rho)(c, \zeta) = G(\zeta)^{(k-1)/2} \langle e_\rho(\zeta), \Phi(c, \mu(\zeta)) \rangle .$$

An operator $X$ on $\mathcal{R}$ and an element $X_{\mathrm{m}}$ of the model algebra *agree under* $e$ if $\mathrm{tr}_e(X \Phi) = X_{\mathrm{m}}\, \mathrm{tr}_e \Phi$ for all $\Phi$.

If $|u_\rho| = 1$, then $e'_\rho = u_\rho e_\rho$ is again a frame and $\mathrm{tr}_{e'} \Phi(\rho) = \bar u_\rho\, \mathrm{tr}_e \Phi(\rho)$. All the changes below are of this kind.

The place carries the *actual operators*, the entries $t_{ab}(Y)$ of an actual $2 \times 2$ matrix of operators on $\mathcal{R}$. An *actual datum* of the place is a normal form datum $\mathsf{d}$ over the operators on $\mathcal{R}$, in the sense of the previous section, whose level is the actual level of the place and a star level, which satisfies the relations of a normal form, and whose matrix $Q_{\mathsf{d}}(Y)$ is the actual matrix for all $Y$.

**Definition 1.4.3 (Transfer frame).** A frame $e$ is a *transfer frame* for an actual datum $\mathsf{d}$ if these operators of $\mathsf{d}$ agree under $e$ with the model operators of the same name: $\zeta^{\pm 1}$, $\bar\zeta^{\pm 1}$, $G^{\pm 1}$, $\nabla$, $\nabla^*$, $\kappa(f)$ for every function $f$ of types, and $S_l$, $S_l^*$ for $1 \le l \le k - 1$.

**Definition 1.4.4 (Rotation hypothesis).** The *rotation hypothesis* (R) states: take a place with the standard section, an actual datum, and a frame $e$ such that each $e_\rho$ is constant on $\Omega$ and every $\kappa(f)$ agrees with the model. Let $R$ be an operator on $\mathcal{R}$ that commutes with every $\kappa(f)$ and acts on the domain as the sum of the diagonal matrix units of the last block plus an integer. Then for each type $\rho$ there is $m \in \mathbb{Z}$ with

$$\mathrm{tr}_e(R\Phi)(\rho) = \zeta\, \partial_\zeta f - \bar\zeta\, \partial_{\bar\zeta} f + m f, \qquad f = \mathrm{tr}_e \Phi(\rho).$$

In polar coordinates $\zeta\partial_\zeta - \bar\zeta\partial_{\bar\zeta} = -i\partial_\theta$, so $R$ acts on transfers as a rotation generator up to an integer. This chapter does not prove (R).

### The theorem

**Theorem 1.4.5 (Transfer frames).** Assume (R). Let $P$ be a parameter with $k \ge 2$, take a place of $P$ with a constant section, and let $\mathsf{d}$ be an actual datum. Then there is a transfer frame for $\mathsf{d}$.

Lean: `Formalism.FourierDecayAlt.P.CutMP.Gauge.GC.genTransfer_of_rotK`

*Proof.* There are four steps.

1. The operators $\zeta^{\pm 1}$, $\bar\zeta^{\pm 1}$, $G^{\pm 1}$ agree with the model under every family $e$: they multiply $\Phi(c, \mu(\zeta))$ by a function of $\zeta$, and this factor passes through the inner product at the same point.
2. There is a frame $e_0$ under which every $\kappa(f)$ agrees with the model: the idempotents $E_\pi = \kappa(\delta_\pi)$ cut each fibre into pieces, and smooth orthonormal bases of the pieces give $e_0$.
3. The gauge theorem for the connection changes $e_0$ to a frame $e_1$ under which $\kappa$, $\nabla$ and $\nabla^*$ agree with the model.
4. The gauge theorem for the raising operators changes $e_1$ to a frame $e$ under which, in addition, $S_l$ and $S_l^*$ agree with the model.

Step 1 holds for $e$ because it holds for every family. $\square$

### The connection

**Lemma 1.4.6 (Locality of the covariant derivatives).** Let $\mathsf{d}$ be an actual datum of a place with a constant section and let $e$ be a frame that carries $\kappa$. There are smooth functions $A_\rho$, $B_\rho$ on $\Omega$ with

$$\mathrm{tr}_e(\nabla \Phi)(\rho) = \partial_\zeta f + A_\rho f, \qquad \mathrm{tr}_e(\nabla^* \Phi)(\rho) = -\partial_{\bar\zeta} f + B_\rho f,$$

for all $\Phi$, where $f = \mathrm{tr}_e \Phi(\rho)$.

Lean: `Formalism.FourierDecayAlt.P.CutMP.Gauge.GC.gauge_locality_holds`

*Proof.* Call an operator on $\mathcal{R}$ *radially local* if the radial part of $X\Phi$ at $(c, \zeta)$ is a finite sum $\sum_{j \le n} C_j(\zeta)$ applied to the $j$-th derivative in $\zeta$ of the radial part of $\Phi$, with smooth $C_j$ on $\Omega$. First, each entry $t_{ab}(Y)$ is radially local; this comes from a finite jet and a Taylor expansion in the radial variable. Second, $\nabla$ and $\nabla^*$ are radially local, because they come from the entries of the actual matrix, the function operators and $\kappa$, which keep the class. Third, the Leibniz rules (D), $\nabla \zeta = \zeta \nabla + 1$ and $\nabla \bar\zeta = \bar\zeta \nabla$, fix the first order part of $\nabla$ as $\partial_\zeta$, and the commutation with $\kappa$ makes the zero order part diagonal in the types. The case of $\nabla^*$ uses (D$^*$). $\square$

**Lemma 1.4.7 (Reference frame).** Assume (R). Let $\mathsf{d}$ be an actual datum of a place with a constant section. There is a frame $e_0$ that carries $\kappa$, with coefficients $A^0_\rho$, $B^0_\rho$, such that $\alpha_\rho = a_\rho \bar\zeta G^{-1} - A^0_\rho$ satisfies for every type $\rho$:

1. $\mathrm{Re}\, \partial_{\bar\zeta} \alpha_\rho = 0$ on $\Omega$;
2. for every $R > 0$ with $R^2 > T_2$ there is $n \in \mathbb{Z}$ with $\mathrm{Im} \oint_{|\zeta| = R} \alpha_\rho\, d\zeta = \pi n$.

Lean: `Formalism.FourierDecayAlt.P.CutMP.Gauge.GC.gTCRef_of_rotK`

*Proof.* The term $a_\rho \bar\zeta G^{-1}$ is the coefficient of the model $\nabla = \partial_\zeta + a_\pi \bar\zeta G^{-1}$. For coefficients $A$, $B$, a direct computation gives $\nabla^* \nabla - \nabla \nabla^* = -(\partial_{\bar\zeta} A_\rho + \partial_\zeta B_\rho)$ on transfers. The level is a star level, so $B_\rho = \bar A_\rho$ and the right side is $-2\, \mathrm{Re}\, \partial_{\bar\zeta} A_\rho$. By [the curvature theorem](/entry/curv/) the left side is $2 a_\rho T_2 G^{-2}$. The model satisfies the same identity, as $\partial_{\bar\zeta}(\bar\zeta G^{-1}) = -T_2 G^{-2}$. The difference gives item 1.

For item 2, take the standard section and a frame constant on $\Omega$ that carries $\kappa$. Apply (R) to the rotation operator of the place; the trace of the curvature identity fixes its zero order term. Compare $R$ with $\zeta \nabla - \bar\zeta \nabla^*$: the difference is multiplication by $\zeta A^0_\rho - \bar\zeta B^0_\rho$ plus an integer, so $\mathrm{Re}(\zeta \alpha_\rho) = n/2$ with $n \in \mathbb{Z}$. On $|\zeta| = R$ we have $d\zeta = i \zeta\, d\theta$, so

$$\mathrm{Im} \oint_{|\zeta| = R} \alpha_\rho\, d\zeta = \int_0^{2\pi} \mathrm{Re}(\zeta \alpha_\rho)\, d\theta = \pi n .$$

A move step, which uses the integrality and the transition properties of the radial gauge, then carries the frame to the given constant section. $\square$

**Theorem 1.4.8 (Gauge for the connection).** Assume (R). Let $\mathsf{d}$ be an actual datum of a place with a constant section and let $e$ be a frame that carries $\kappa$. There is a frame $e'$ under which $\kappa(f)$, $\nabla$ and $\nabla^*$ agree with the model.

Lean: `Formalism.FourierDecayAlt.P.CutMP.Gauge.GC.gTConn_of_rotK`

*Proof.* Take $A_\rho$, $B_\rho = \bar A_\rho$ from the locality lemma and put $\alpha_\rho = a_\rho \bar\zeta G^{-1} - A_\rho$.

First, items 1 and 2 of the reference lemma hold for $\alpha_\rho$. Both $e$ and $e_0$ carry $\kappa$, so $e_\rho = v_\rho\, e_{0, \rho}$ with $|v_\rho| = 1$, and $A_\rho = A^0_\rho + \bar v_\rho \partial_\zeta v_\rho$. Locally $v_\rho = e^{i\phi}$ with $\phi$ real, so $\bar v_\rho \partial_\zeta v_\rho = i \partial_\zeta \phi$. Here $\mathrm{Re}\, \partial_{\bar\zeta}(i\partial_\zeta\phi) = 0$ because $\partial_{\bar\zeta}\partial_\zeta\phi$ is real, and $\mathrm{Im}\oint i\partial_\zeta\phi\, d\zeta = \frac12 \oint d\phi \in \pi\mathbb{Z}$.

Second, the real one form $\omega = 2\, \mathrm{Im}(\alpha_\rho\, d\zeta)$ is closed by item 1, and its periods on the annulus $\Omega$ lie in $2\pi\mathbb{Z}$ by item 2. So there is a smooth $\theta$ with $d\theta = \omega$, unique up to $2\pi\mathbb{Z}$, and $u_\rho = e^{i\theta}$ is smooth on $\Omega$. The $(1,0)$ part of $d\theta = \omega$ is $\partial_\zeta \theta = -i\alpha_\rho$, so $\bar u_\rho \partial_\zeta u_\rho = \alpha_\rho$.

Put $e'_\rho = u_\rho e_\rho$. With $f = u_\rho f'$,

$$\mathrm{tr}_{e'}(\nabla \Phi)(\rho) = \partial_\zeta f' + \bigl(A_\rho + \bar u_\rho \partial_\zeta u_\rho\bigr) f' = \partial_\zeta f' + a_\rho \bar\zeta G^{-1} f' ,$$

which is the model $\nabla$. The conjugate computation gives the model $\nabla^*$. The phase acts type by type, so $\kappa$ is kept. $\square$

### The raising operators

**Theorem 1.4.9 (Raising operators, with locality and adjoint).** Assume:

1. *adjoint*: for every actual datum and every frame that carries $\kappa$, if $S_l$ and $S_l^*$ act on transfers by matrices of smooth functions $s_l(\rho', \rho)$ and $t_l(\rho', \rho)$, then $t_l(\rho', \rho) = \overline{s_l(\rho, \rho')}$ on $\Omega$;
2. *radial locality*: every entry $t_{ab}(Y)$ of the actual matrix is radially local.

Let $\mathsf{d}$ be an actual datum of a place with a constant section and let $e$ be a frame under which $\kappa(f)$, $\nabla$ and $\nabla^*$ agree with the model. There is a frame $e'$ under which, in addition, $S_l$ and $S_l^*$ agree with the model for $1 \le l \le k - 1$.

Lean: `Formalism.FourierDecayAlt.P.CutMP.Gauge.GC.gTSS_of_adj_radT`

*Proof.* First, by radial locality and condition 3 of a normal form, $S_l$ and $S_l^*$ are radially local of order zero, so they act on transfers by matrices $s_l$, $t_l$ of smooth functions. Second, the relation (S), $\nabla S_l = S_l \nabla - \bar\zeta G^{-1} S_l$, reads on transfers

$$\partial_\zeta s_l(\rho', \rho) + (a_{\rho'} - a_\rho + 1)\, \bar\zeta G^{-1} s_l(\rho', \rho) = 0 .$$

By (Sh), $s_l(\rho', \rho) = 0$ unless $\rho \to_l \rho'$, and then $a_{\rho'} = a_\rho - 1$, so $\partial_\zeta s_l = 0$. The relation for $\nabla^*$ gives $\partial_{\bar\zeta} s_l = 0$. So $s_l$ and $t_l$ are constant on the connected set $\Omega$. Third, by hypothesis 1 the matrix $t_l$ is $s_l^*$. Last, the phase theorem below gives $e'$. $\square$

**Theorem 1.4.10 (Raising operators, with adjoint).** Under hypothesis 1 of the previous theorem alone, the same conclusion holds.

Lean: `Formalism.FourierDecayAlt.P.CutMP.Gauge.GC.gTSS_of_adj`

*Proof.* Hypothesis 2 is the first step in the proof of the locality lemma. $\square$

**Theorem 1.4.11 (Gauge for the raising operators).** Let $\mathsf{d}$ be an actual datum of a place with a constant section and let $e$ be a frame under which $\kappa(f)$, $\nabla$ and $\nabla^*$ agree with the model. There is a frame $e'$ under which $\kappa(f)$, $\nabla$, $\nabla^*$, $S_l$ and $S_l^*$ agree with the model for $1 \le l \le k - 1$.

Lean: `Formalism.FourierDecayAlt.P.CutMP.Gauge.GC.second_shift_gauge_holds`

*Proof.* The adjoint hypothesis holds: at each $\zeta$ the Hilbert-Schmidt product makes the star of the level the adjoint, so in the orthonormal basis $e_\rho(\zeta)$ the matrix of $S_l^*$ is the conjugate transpose of that of $S_l$. Apply the previous theorem. $\square$

**Theorem 1.4.12 (The phase of the raising operators).** Let $P$ be admissible, let $\mathsf{d}$ be an actual datum of a place, and let $e$ be a frame under which $\kappa(f)$, $\nabla$, $\nabla^*$ agree with the model. Assume that $S_l$ and $S_l^*$ act on transfers by constant matrices $s_l$ and $s_l^*$ for $1 \le l \le k - 1$. Then there are $u(\rho)$ of modulus one such that under $e'_\rho = u(\rho)\, e_\rho$ all of $\kappa(f)$, $\nabla$, $\nabla^*$, $S_l$, $S_l^*$ agree with the model.

Lean: `Formalism.FourierDecayAlt.P.CutMP.Gauge.GC.SSPh.second_shift_phase_holds`

*Proof.* There are five steps.

1. *Support.* By (Sh), $s_l(\rho', \rho) = 0$ unless $\rho \to_l \rho'$. Write $s_l(\rho) = s_l(\rho + e_l, \rho)$.
2. *Norm.* By condition 6, $S_l^* S_l = \kappa(N_l)$, so $|s_l(\rho)|^2 = N_l(\rho)$. Where $N_l(\rho) > 0$ put $w_l(\rho) = s_l(\rho) / \sqrt{N_l(\rho)}$, of modulus one.
3. *Commutation.* The actual matrix of a place is a start, and it is the matrix of $\mathsf{d}$, so [the extra relations](/entry/shift-extra/) hold. Part 3 gives $S_j S_l\, \kappa(\rho_j - \rho_l - 1) = S_l S_j\, \kappa(\rho_j - \rho_l + 1)$ for $j \ne l$.
4. *Cocycle.* Take the entry of part 3 from $\rho$ to $\rho + e_j + e_l$. For $j \ne l$ the coordinates of a type satisfy $|\rho_j - \rho_l| \ge 2$, so $\rho_j - \rho_l \pm 1 \ne 0$. The same identity holds in the model with the entries $\sqrt{N_l}$; dividing removes the scalars and leaves $w_j(\rho + e_l)\, w_l(\rho) = w_l(\rho + e_j)\, w_j(\rho)$ whenever both paths exist.
5. *Phase.* By induction on $\sum_i \rho_i$ there is $u$ with $u(\rho + e_l)\, \overline{u(\rho)} = w_l(\rho)$ for all $l$ and $\rho$: at a new type the possible values agree by the cocycle identity. Under $e'$ the matrix of $S_l$ becomes $\overline{u(\rho + e_l)}\, s_l(\rho)\, u(\rho) = \sqrt{N_l(\rho)}$, the model entry, and $S_l^*$ follows by adjoints. The phases are constant and act type by type, so $\nabla$, $\nabla^*$ and $\kappa$ are kept. $\square$

**Remark 1.4.13 (Formalization).** The rotation hypothesis is stated only for the standard section (`HermitianCurvatureProofs/CutGCoreGTRRotCut.lean:30`), so the reference frame needs a move step to reach a general constant section. In `HermitianCurvatureProofs/CutGCoreDone.lean:31` the connection theorem builds the reference frame twice from the same hypothesis, once for the curvature condition and once for the holonomy condition. The adjoint hypothesis asks for the relation at every point of $\Omega$ (`HermitianCurvatureProofs/CutGCoreGTSSCut.lean:49`), but the phase step uses only the point $\zeta_0 = \sqrt{T_2} + 1$ (`HermitianCurvatureProofs/CutGCoreGTSSPhase.lean:70`). The radial locality hypothesis of `HermitianCurvatureProofs/cut_GCore_GTSS.lean:9` is filled at line 12 by the lemma that the locality lemma also uses, so this layer adds no content. The statement for the function operators holds for every family, frame or not (`HermitianCurvatureProofs/CutGCoreGenTransferCut.lean:57`). The phase theorem destructures the constant section and the actual level hypotheses at `HermitianCurvatureProofs/CutGCoreGTSSPhase.lean:67` and never uses them.

---
title: The kernel part laws of column pins
decls:
  - GlobalTheory.KerLaws.clsKL_is
  - GlobalTheory.T.kernelPart_laws_of_columnPins
status: drafted
drafted_by: writer@claude-opus-5-5
---
## The kernel part laws of column pins

A pinned column of a twisted tower gives a *kernel class datum*: for each step and each column character, a level group, a character of it, representatives of the classes, the values of the forms at the classes, and linear forms between classes. This section proves the five laws that make this datum good. The core law is [the theta kernel identity](/entry/kernel-identity-tuple/) of the last section. The other four laws come from results on the true column tuple that we cite. The theorem is step 3 of [class data from the column condition](/entry/cls-pin-d-of-fam-col-of-true-w/) in the open orbit chapter.

**Setting.** We keep the notation of [the last section](/entry/kernel-identity-tuple/): a valid twisted tower $I$ with pinned data, laws $l$, later data $Z$, a word $u$ and an index $a$, a twist datum $A$, live maps $\iota_j$ from the column characters $\mathrm{Ch}_j$ into the characters of $A$, and the linear forms $\mathrm{ab}_j$. Let $R$ be a real datum with additive character $\psi$ and infinite family $\theta$, and let $g$ be a geometric datum with level data $x_j$ and vacua $f_j$. Let $c_0, s \colon \mathbb{N} \to \mathbb{C}$. The *real datum* of $(R, g, s)$ has the ranks $N_j$ of the column chain, the dominant weights $\lambda_j$ of the word $u$, real points $k \mapsto r_j(k)$, the exponents $s^\sharp_j$ and $s^{\mathrm{div}}_j$ of the chain, and the scales $\sigma_j(\tau) = s_j / c_D(\tau)$ when $s_j \neq 0$ (and $1$ otherwise). Let $t$ be the tuple of a level polynomial, a row choice and a column choice $k$. It gives the kernel operators $K_j$, the ramified forms $\mathrm{Ram}_j$, their readings, the finite combinations $d_j$, the core constants $c_K(j)$, and the kernel vectors at each pair of characters.

**Definition 2.22.1 (Kernel class datum).** The kernel class datum of $(A, \iota)$ assigns to a step $j$ and a character $\beta \in \mathrm{Ch}_j$:

1. the classes $c$ of step $j$ with character $\iota_j \beta$;
2. the group $U_j(\iota_j \beta)$, its character $\chi_j(\iota_j \beta)$, and the representatives $h_j(\iota_j \beta, c)$;
3. the value $\phi(c)$ at a class $c$ of a form $\phi$, as a function on the frames;
4. the linear form $\mathrm{ab}_j(c, c')$ at a pair of classes.

The datum is *good* if it has five properties.

1. *Forms.* For $j \leq m$, the $h_j(\beta, c)$ represent the double cosets of $U_j(\beta)$, each once; each $\chi_j(\beta)$ is continuous; each value of a ramified form lies in the space of $\lambda_j$; and the reading of a ramified form at $\gamma\, h_j(\beta, c)\, k\, \kappa$, with $\gamma$ rational, $k$ in the compact infinite group and $\kappa \in U_j(\beta)$, is $\chi_j(\beta)(\kappa)$ times the value at the point moved by $r_j(k)$.
2. *Real.* For $j + 1 \leq m$ and real points $(k, k')$, the kernel at $(k, k')$ applied to the kernel vector of a polynomial $P$ is
$$\prod_\tau \det r_j(k)_\tau^{\,s^\sharp_j(\tau)}\ \det r_{j+1}(k')_\tau^{\,-s^{\mathrm{div}}_j(\tau)}$$
times the kernel vector of $P'$, where $P'$ is $P$ moved by $r_j(k)^{-1}$ and $r_{j+1}(k')$.
3. *Level.* For $j < m$, $\kappa \in U_j(\alpha)$ and $\kappa' \in U_{j+1}(\gamma)$, the pair $(\kappa, \kappa')$ acts on the combination of $d_j(\alpha, \gamma)$ applied to $f_j$ by the scalar $\chi_j(\alpha)(\kappa)^{-1}\, \chi_{j+1}(\gamma)(\kappa')$.
4. *Core.* For $j + 1 \leq m$, classes $c$ and $c'$ and a polynomial $P$,
$$\mathrm{vol}(U_j(\alpha))\ \theta_K\big(h_j(\alpha, c), h_{j+1}(\gamma, c')\big)(P \cdot F) = c_K(j)\ \mathrm{ab}_j(c, c')(P_\sigma),$$
where $F$ is the kernel vector of $(\alpha, \gamma)$ and $P_\sigma$ is $P$ with the variables at $\tau$ scaled by $\sigma_j(\tau)$.
5. *Values.* For $j < m$ with $N_j \leq N_{j+1}$, a ramified form $\phi$, and polynomials $F_{\alpha, c}$ in the space of $(\lambda_j, n_j)$ with $\phi(c)(y) = F_{\alpha, c}(y) \prod_\tau \det y_\tau^{-s^\sharp_j(\tau)}$, the value of $K_j \phi$ at a class $c'$ of step $j + 1$ and a frame $y'$ is
$$\sum_\alpha \sum_c \frac{1}{|\mathrm{Stab}(c)|}\ \mathrm{ab}_j(c, c')\big(F_{\alpha, c}|_{y'}\big) \prod_\tau \det y'^{\,-s^{\mathrm{div}}_j(\tau)}_\tau.$$
Here $\mathrm{Stab}(c)$ is the stabilizer of the class $c$ in $U_j(\alpha)$, and $F|_{y'}$ is the restriction of $F$ to the first $N_j$ rows of $y'$.

**Theorem 2.22.2 (Kernel part laws).** Let $I$ be a valid twisted tower with pinned data. Assume pin data for $(\psi, \theta, x, f, c_0)$, the jet law for $s$, a good level datum $x_j$ for each $j \leq m$, and a pinned column for $(A, \iota)$ with weights $w$. Then the kernel class datum of $(A, \iota)$ is good.

Lean: `GlobalTheory.KerLaws.clsKL_is` (also `GlobalTheory.T.kernelPart_laws_of_columnPins`, a second name).

The *jet law* for $s$ says that for each $j + 1 \leq m$, $s_j \neq 0$ and $(P \cdot f)(0) = j_{s_j}(\xi(f), P)$ for every holomorphic $f$ on the Weil space of $(X_j, X_{j+1})$.

*Proof.* We prove the five properties in turn.

1. *Forms.* The theorem on chart representatives gives, for $j \leq m$ and the character $\iota_j \beta$ of $A$, that the $h_j$ represent the double cosets and that $\chi_j$ is continuous. It uses only the first field of the pinned column. For a ramified form $\phi$, the ramified field of the pinned column gives that $\phi$ is ramified for the chain. The theorem on scalar forms on the charts of the true column tuple then gives that the values lie in the space of $\lambda_j$, and gives the transformation law of the reading at $\gamma\, h\, k\, \kappa$. The reading field of the pinned column identifies the reading of the tuple with the reading in that theorem. The moved point matches because the infinite level datum is trivial at $x_j$, so the scale in the real point is $1$.
2. *Real.* This is the theorem on kernel vectors at real points, with all the hypotheses.
3. *Level.* This is the theorem on the action of level pairs on the finite datum.
4. *Core.* Fix $j + 1 \leq m$. The jet law gives $s_j \neq 0$ and the jet identity on holomorphic functions. Since $s_j \neq 0$, $\sigma_j(\tau) = s_j / c_D(\tau)$, so $P_\sigma$ is the rescaled polynomial of [the last section](/entry/kernel-identity-tuple/). The pin data give the volume and the trivial infinite parts of $x_j$ and $x_{j+1}$, so the kernel and the volume of the class datum are those of that theorem. Its conclusion is the core law.
5. *Values.* This is the theorem that the kernel of the live charts is a sum of jets over classes, with all the hypotheses. $\square$

**Remark 2.22.3 (Formalization).** The theorem is at [KernelPartLawsOfColumnPins.lean](lean:Development/AbelianVarietyTheory/Proofs/DecoratedLatticeProofs/KernelPartLawsOfColumnPins.lean#L22). The second name is in [KernelPartLawsOfColumnPinsStatement.lean](lean:Development/AbelianVarietyTheory/Proofs/DecoratedLatticeProofs/KernelPartLawsOfColumnPinsStatement.lean#L9), by a `first | exact` block under one million heartbeats. The kernel class datum and its five laws are in [OnFramesRdApply.lean](lean:Development/AbelianVarietyTheory/Definitions/LatticeFrames/OnFramesRdApply.lean#L69), the datum of a pinned column in [PinColL.lean](lean:Development/AbelianVarietyTheory/Definitions/LatticeFrames/PinColL.lean#L49), and the real datum with its scales in [RealOf.lean](lean:Development/AbelianVarietyTheory/Definitions/LatticeFrames/RealOf.lean#L30). The jet law is at line 18 of that file. The scale is $1$ when $s_j = 0$, but the jet law excludes this case for $j + 1 \leq m$, so the default never enters the core law. Of the pinned column, the proof uses three fields directly: the representatives, the ramified forms and the readings (lines 38 to 50). The hypothesis that each $x_j$ is good is used only by the cited theorems for the real and value laws (lines 51 and 52). The five cited theorems are restatements in files of the same folder. We have read their statements, not their proofs.
